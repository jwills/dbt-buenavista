import json

from dbt.contracts.connection import AdapterResponse


def submit(connection, parsed_model: dict, compiled_code: str) -> AdapterResponse:
    identifier = parsed_model["alias"]
    payload = {
        "ext": "dbt_python_job",
        "module_name": identifier,
        "module_definition": compiled_code,
    }
    res = connection.handle.execute(json.dumps(payload))
    return AdapterResponse(_message=res[0][0])
