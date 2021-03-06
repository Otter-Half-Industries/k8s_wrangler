# Kubernetes Wrangler

## Prerequisites

Note that this project has only been tested on MacOS Catalina v10.15.4 with VMWare Fusion v11.5.3.

- [ ] Docker v19.03.8 [installed](https://docs.docker.com/get-docker/) and configured
- [ ] kubectl [installed](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [ ] Minikube v1.9.2 [installed](https://kubernetes.io/docs/tasks/tools/install-minikube/) and configured
- [ ] A Minikube [driver](https://minikube.sigs.k8s.io/docs/drivers/) installed and configured - VMWare was used to test, and as of May 14, 2020 is available for a 30 day free trial before a paid subscription
- [ ] Kubernetes v1.14.0:
`minikube start -p k8s-v1.14.0 --kubernetes-version v1.14.0`
- [ ] Kubernetes v1.16.0:
`minikube start -p k8s-v1.16.0 --kubernetes-version v1.16.0`

## Installation

Once all prerequisites have been installed and configured:

1. Locally navigate to the directory you'd like to clone this repo to, clone the repo and enter it:
```bash
git clone git@github.com:Otter-Half-Industries/k8s_wrangler.git
cd k8s_wrangler
```

2. Confirm your installation by making sure the tests are working:
```bash
cd app
pytest -vv
```

## Usage

After running `minikube start --kubernetes-version <version> --driver=<driver>` (where `<version>` is the version of Kubernetes you'd like to try, and `<driver>` is whichever minikube driver you've installed and configured), it is possible to test some scenarios.

Scenario 1: Run Kubernetes Wrangler locally.

1. Locally navigate to `k8s_wrangler/app`.
2. Using `virtualenv` create a virtual environment, activate it, and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run the Kubernetes Wrangler server:
```bash
python app.py
```
4. In a browser, try the endpoints at `localhost:5000/deployments` and `localhost:5000/pods`.

Scenario 2: Run Kubernetes Wrangler in a Docker Container

1. Locally navigate to `k8s_wrangler/`
2. Build and tag the docker container:
```bash
docker build -t k8s-wrangler:1.14.0 .
```

3. Run the Docker container to start the Kubernetes Wrangler server:
```bash
docker run k8s-wrangler:1.14.0
```
4. In a browser, try the endpoints at `0.0.0.0:5000/deployments` and `0.0.0.0:5000/pods`

## Building the docker image for k8s clusters

### k8s v1.14.0
```bash
kubectl config use-context k8s-v1.14.0
eval $(minikube -p k8s-v1.14.0 docker-env)
docker build -t k8s-wrangler:1.14.0 .
```

### k8s v1.16.0
```bash
kubectl config use-context k8s-v1.16.0
eval $(minikube -p k8s-v1.16.0 docker-env)
docker build -t k8s-wrangler:1.16.0 .
```

## deploying the apps to k8s
```bash
kubectl apply -f deployment_rbac.yml
```

Exposing and connecting the application:

### k8s v1.14.0
```bash
kubectl config use-context k8s-v1.14.0
kubectl expose deployment -n chipy k8s-wrangler --type=LoadBalancer --port=5000
minikube service -p k8s-v1.14.0 -n chipy k8s-wrangler
```

### k8s v1.16.0
```bash
kubectl config use-context k8s-v1.16.0
kubectl expose deployment -n chipy k8s-wrangler --type=LoadBalancer --port=5000
minikube service -p k8s-v1.16.0 -n chipy k8s-wrangler
```
