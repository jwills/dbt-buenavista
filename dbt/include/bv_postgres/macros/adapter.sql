
{% macro bv_postgres__create_table_as(temporary, relation, compiled_code, language='sql') -%}
  {%- if language == 'sql' -%}
    {%- set sql_header = config.get('sql_header', none) -%}

    {{ sql_header if sql_header is not none }}

    create {% if temporary: -%}temporary{%- endif %} table
      {{ relation.include(database=False, schema=(not temporary)) }}
    as (
      {{ compiled_code }}
    );
  {%- elif language == 'python' -%}
    {{ py_write_table(temporary=temporary, relation=relation, compiled_code=compiled_code) }}
  {%- else -%}
      {% do exceptions.raise_compiler_error("bv_postgres__create_table_as macro didn't get supported language, it got %s" % language) %}
  {%- endif -%}
{% endmacro %}

{% macro py_write_table(temporary, relation, compiled_code) -%}
{{ compiled_code }}

def materialize(df, con):
    import pandas as pd
    import io
    tbl = ".".join([ "{{ relation.schema }}", "{{ relation.identifier }}"])
    create_table_stmt = pd.io.sql.get_schema(df, "__placeholder__").replace("\"__placeholder__\"", tbl)
    con.execute(create_table_stmt)

    output = io.StringIO()
    df.to_csv(output, na_rep='null', header=False, index=False)
    output.seek(0)
    with con.copy(f"COPY {tbl} FROM STDIN WITH DELIMITER ',' NULL AS 'null' CSV") as copy:
        while data := output.read(8192):
            copy.write(data)
{% endmacro %}

