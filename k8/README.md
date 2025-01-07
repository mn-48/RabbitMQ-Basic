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

#### describe secret vars
```
kubectl describe secret shop-secret
```

#### run deployment.yml
```
kubectl apply -f deployment.yml
```
#### describe secret vars
```
kubectl apply -f svc.yml
```

