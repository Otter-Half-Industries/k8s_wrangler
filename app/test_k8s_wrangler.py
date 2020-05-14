import pytest
from k8s_wrangler import K8sWrangler

class TestK8sWrangler:
    def setup(self):
        self.kw = K8sWrangler()

    def test_get_pods(self):
        assert self.kw.get_pods() == {'echoserver': '1.4'}

    def test_get_deployments(self):
        assert self.kw.get_deployments() == {}
