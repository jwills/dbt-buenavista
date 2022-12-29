import time

from dbt.contracts.connection import AdapterResponse
import requests


def submit(connection, credentials, parsed_model: dict, compiled_code: str, wait_time_secs: int = 300) -> AdapterResponse:
    process_id = connection.handle.get_backend_pid()
    base_url = f"http://{credentials.host}:{credentials.api_port}"
    identifier = parsed_model["alias"]
    body = {
        "process_id": process_id,
        "module_name": identifier,
        "module_definition": compiled_code,
    }

    resp = requests.post(f"{base_url}/submit_dbt_python_job", json=body)
    if resp.ok:
        payload = resp.json()
        if payload["ok"]:
            check_endpoint = f"{base_url}/check_dbt_job_status"
            cnt = 0
            while cnt < wait_time_secs:
                time.sleep(1)
                resp = requests.get(
                    check_endpoint, params={"process_id": process_id}
                )
                cnt += 1
                if resp.ok:
                    payload = resp.json()
                    if payload["ok"]:
                        if payload["status"] == "Success":
                            return AdapterResponse(_message="OK")
                    else:
                        return AdapterResponse(_message=payload["status"])
                else:
                    raise Exception("Check job status failed: " + str(resp))
            return AdapterResponse(_message="Timeout")
        else:
            raise Exception(
                "Initial request had status failure: " + payload["status"]
            )
    else:
        raise Exception("Initial request failed: " + str(resp))
