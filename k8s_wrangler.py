from kubernetes import client, config

nodes = ['192.168.64.3']

class KubernetesWrangler:
    def __init__(self):
        self.deployments = {}

    def connect(self):
        config.load_kube_config()
        v1 = client.CoreV1Api()
        return v1

    def get_pods(self):
        pods = []
        conn = self.connect()
        ret = conn.list_pod_for_all_namespaces(watch=False)
        for item in ret.items:
            if item.status.pod_ip not in nodes:
                pods.append(item.status.pod_ip)
        return pods

    def get_deployments(self):
        # conn = self.connect()
        return self.deployments
