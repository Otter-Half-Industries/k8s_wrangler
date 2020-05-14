import traceback
from kubernetes import client, config

class K8sWrangler:
    def __init__(self):
      try:
        self.config = config.load_kube_config()

      except Exception:
        print("local config not found attempting incluster config", flush=True)

        # if we can't find local kube_config, try the incluster_config
        try:
          self.config = config.load_incluster_config()
        except Exception:
          print(f"Error: {traceback.format_exc()}")

      self.core_v1_api = client.CoreV1Api()

      # k8s 1.14.0
      self.extensions_v1_beta1_api = client.ExtensionsV1beta1Api()

      # k8s 1.16.0+
      #self.apps_v1_api = client.AppsV1Api()

    def get_pods(self, namespace="chipy"):
        pod_versions = {}

        try:
          ret = self.core_v1_api.list_namespaced_pod(namespace, timeout_seconds=30)

          for item in ret.items:
            container_vals = item.spec.containers[0].image.split(':')
            container_name = container_vals[0]
            container_version = container_vals[1]
            pod_versions[container_name] = container_version

        except Exception as e:
          print(f"Error: {traceback.format_exc()}")

        return pod_versions

    def get_deployments(self, namespace="chipy"):
        deployment_versions = {}

        try:
          # k8s 1.14.0
          ret = self.extensions_v1_beta1_api.list_namespaced_deployment(namespace, timeout_seconds=30)

          # k8s 1.16.0+
          #ret = self.apps_v1_api.list_namespaced_deployment(namespace, timeout_seconds=30)

          for item in ret.items:
            container_vals = item.spec.template.spec.containers[0].image.split(':')
            container_name = container_vals[0]
            container_version = container_vals[1]
            deployment_versions[container_name] = container_version

        except Exception as e:
          print(f"Error: {traceback.format_exc()}")

        return deployment_versions

# useful for local debugging
if __name__ == "__main__":
  kw = K8sWrangler()
  print(kw.get_pods())
  print(kw.get_deployments())
