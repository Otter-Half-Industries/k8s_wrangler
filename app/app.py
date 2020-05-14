import json
from flask import Flask
from k8s_wrangler import K8sWrangler

app = Flask(__name__)

@app.route('/deployments')
def deployments():
    k8s_wrangler = K8sWrangler()
    deployments = k8s_wrangler.get_deployments()

    return json.dumps(deployments)

@app.route('/pods')
def pods():
    k8s_wrangler = K8sWrangler()
    pods = k8s_wrangler.get_pods()

    return json.dumps(pods)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
