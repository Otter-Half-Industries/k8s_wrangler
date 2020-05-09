from kubernetes import client, config

class KubernetesWrangler:
    def __init__(self):
        self.deployments = {}

    def connect(self):
        config.load_kube_config()
        v1 = client.CoreV1Api()
        return v1

    def get_pods(self, namespace="default"):
        try:
          pods = {}
          conn = self.connect()
          ret = conn.list_namespaced_pod(namespace, timeout_seconds=90, limit=25)
          for item in ret.items:
            container_vals = item.spec.containers[0].image.split(':')
            container_name = container_vals[0].split('/')[1]
            container_version = container_vals[1].strip("'")
            pods[container_name] = container_version
          return pods
        except Exception as e:
          print({'Error': e})

    def get_deployments(self):
        # conn = self.connect()
        return self.deployments

if __name__ == "__main__":
  kw = KubernetesWrangler()
  kw.get_pods()
