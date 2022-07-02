import pytest
import readonly_github_sdk.endpoints as endpoints
import readonly_github_sdk.model as model

@pytest.mark.vcr()
def test_pagination():
    assert endpoints.get_followers("foo") == endpoints.get_followers("foo", params={"num_pages": 1})