import json
from flask import Flask
from k8s_wrangler import KubernetesWrangler

app = Flask(__name__)

@app.route('/deployments')
def deployments():
    deployments = json.dumps(KubernetesWrangler().get_deployments())
    return deployments

@app.route('/pods')
def pods():
    pods = json.dumps(KubernetesWrangler().get_pods())
    return pods

if __name__ == "__main__":
    app.run(host='0.0.0.0')
