import json
from flask import Flask
from k8s_wrangler import KubernetesWrangler

app = Flask(__name__)

@app.route('/deployments')
def deployments():
    deployments = json.dumps(KubernetesWrangler().get_deployments())
    return deployments
