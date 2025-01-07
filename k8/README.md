#### Start minikube
```
minikube start
```

#### get all pods
```
kubectl get all
```

#### run  config-map.yml
```
kubectl apply -f config-map.yml
```
#### run secret
```
kubectl create secret generic shop-secret --from-env-file=.env-kuber
```
#### get secret
```
kubectl get secret
```
