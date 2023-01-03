import json

from dbt.contracts.connection import AdapterResponse


def submit(adapter, parsed_model: dict, compiled_code: str) -> AdapterResponse:
    identifier = parsed_model["alias"]
    payload = {
        "ext": "dbt_python_job",
        "module_name": identifier,
        "module_definition": compiled_code,
    }
    response, _ = adapter.execute(json.dumps(payload), auto_begin=False, fetch=False)
    return response
