import pytest
import readonly_github_sdk.endpoints as endpoints
import readonly_github_sdk.model as model

# @pytest.mark.vcr()
def test_pagination():
    """Test that getting results 1 at a time gives same output as getting all at once"""
    assert endpoints.get_followers("foo") == endpoints.get_followers(
        "foo", params={"num_pages": 1}
    )


@pytest.mark.vcr()
def test_repo_owner():
    u = model.User("foo")
    repos = u.repos
    assert len(repos) > 0
    for r in repos:
        assert r.owner.username == "foo"
