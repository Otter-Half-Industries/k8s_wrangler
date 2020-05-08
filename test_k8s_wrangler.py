import pytest
from k8s_wrangler import KubernetesWrangler

class TestK8sWrangler:
    def setup(self):
        self.kw = KubernetesWrangler()
    
    def test_get_pods(self):
        assert self.kw.get_pods() == []

    def test_get_deployments(self):
        assert self.kw.get_deployments() == {}
