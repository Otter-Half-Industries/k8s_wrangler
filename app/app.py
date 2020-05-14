import json
from flask import Flask, jsonify
from k8s_wrangler import K8sWrangler

app = Flask(__name__)

@app.route('/deployments')
def deployments():
    k8s_wrangler = K8sWrangler()
    deployments = k8s_wrangler.get_deployments()

    return jsonify(deployments)

@app.route('/pods')
def pods():
    k8s_wrangler = K8sWrangler()
    pods = k8s_wrangler.get_pods()

    return jsonify(pods)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
