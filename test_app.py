import pytest

class TestApp:
    def setup(self):
        self.app = app.test_client()
    
    def test_deployments(self):
        r = self.app.get('/deployments')
        assert r.status_code == 200
