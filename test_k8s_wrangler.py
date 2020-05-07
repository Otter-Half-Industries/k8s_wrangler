import pytest
from k8s_wrangler import KuberenetesWrangler

class TestK8sWrangler:
    def setup(self):
        self.kw = KubernetesWrangler()

    def test_get_deployments(self):
        assert self.kw == ''
