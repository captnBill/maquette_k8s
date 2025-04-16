# E5 DEVSECOPS projet

## setup instructions

### start minikube

`minikube start --listen-address=0.0.0.0 --memory=max --cpus=max --kubernetes-version=v1.32.0`

`minikube addons enable ingress`

### build docker images

`eval $(minikube docker-env)`

then

`docker build -t django-app:latest apps/appDjango/`

`docker build -t app-8080:latest apps/app8080/`

`docker build -t app-9090:latest apps/app9090/`

check if successful with `docker images`; output should contain `app-9090`, 
`app-8080` and 
`django-app` 

### build k8s components

`kubectl apply -f manifests/namespace.yml`


`kubectl apply -f manifests/ --recursive`

then check with
`kubectl get all --namespace=client-demo`

all apps should be available to access upon forwarding ports
django app should be available through ingress with `django.local`

## components

### namespace

all components are initialized within the namespace `client-demo` and as such can be viewed with

`kubectl get all --namespace=client-demo`

### simple python apps

simple "hello world" type single page applications. 

deployed with a standard deployment with no (1) replicas. Can be modified for scalability. 

accessible via a load balancer service.

### django app

basic starter django project

deployed with a standard deployment with no (1) replicas. Can be modified for scalability.

accessible via ingress at `django.local`

