# Flask app
### Create and build docker container


docker build -t hello-world-app .


docker run -p 5000:5000 hello-world-app



docker tag hello-world-app mdnazmulhossain/hello-world-app:v1
docker push mdnazmulhossain/hello-world-app:v1



### Push Image to dockerhub -------------
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname

docker tag hello-world-app mdnazmulhossain/hello-world-app:v1
docker push mdnazmulhossain/hello-world-app:v1


### deploy public docker-container to kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml


### minikube get sercices 

```
minikube service --all
```

#### for private docker container

1. Set credentials
```
kubectl create secret docker-registry regcred \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=<your-dockerhub-username> \
  --docker-password=<your-dockerhub-password> \
  --docker-email=<your-email>

```

### 2.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world-container
        image: <your-dockerhub-username>/hello-world-app:v1
        ports:
        - containerPort: 5000
      imagePullSecrets:
      - name: regcred

```




docker pull mdnazmulhossain/hello-world-app



docker tag hello-world-app <your-dockerhub-username>/hello-world-app:v1
