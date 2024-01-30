from everstage_api_wrapper import EverstageAPIWrapper


import json


def everstage_api_task():
    url = "http://host.docker.internal:8000/airflow/connector/get-datasheet-names"
    email = "test@datasheet.graph"
    client_id = 3001

    payload = json.dumps({"email": email, "client_id": client_id})

    api_invoker = EverstageAPIWrapper()
    response = api_invoker.session.get(url, data=payload)

    if response.ok:
        print("RECEIVED TABLE NAMES FROM EVERSTAGE API")
        print("response", response)
        print("response.json()", json.dumps(response.json(), indent=4))
    else:
        print("FAILED TO RECEIVE TABLE NAMES FROM EVERSTAGE API")
        print("response", response)
