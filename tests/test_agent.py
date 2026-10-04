from fastapi.testclient import TestClient
from csolarch.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'honor the shared vpc constraint', **{'payload': {'constraint': 'must use the shared vpc'}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["modules"][0] == "private_gke"
    refused = client.post("/agent/run", json={"goal": 'provision this in the customer project'}).json()
    assert refused["refused"] is True
