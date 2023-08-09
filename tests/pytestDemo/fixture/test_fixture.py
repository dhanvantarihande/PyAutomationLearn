# Fixture
# They are used to provide the Data or We can say Setup Operations

# We can use fixture to Setup Data or resources that are needed by multiple tests
# and then use the fixture's  return value in your test functions.

import pytest

@pytest.fixture
def get_token():
    return ("Reyansh","Hande")


def test_put_req(get_token):
    print(get_token)



def test_delete_req(get_token):
    print(get_token)




