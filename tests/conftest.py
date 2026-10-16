import pytest
from app.api import create_app

@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as test_client:
        yield test_client
