import pytest

@pytest.yield_fixture(scope="session",autouse=True)
def InsertToDB():
    print("Running Setting Up")

    yield
    print("Running method level tearDown")
