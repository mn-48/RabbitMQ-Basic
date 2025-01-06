docker-compose up

docker-compose up --build

docker-compose down
# ---------------------------------------------
sudo chmod -R 755 data

chown -R $USER:$USER data

sudo chmod -R 755 data
chown -R $USER:$USER data

sudo chmod -R 755 data
chown -R $USER:$USER data

# ----------------------------------------------
sudo chmod -R 755 SOA/A/data
chown -R $USER:$USER SOA/A/data

sudo chmod -R 755 SOA/B/data
chown -R $USER:$USER SOA/B/data
# -----------------------------------------------
chmod +x shell.sh






# ---- kubernetes --------------

### check version
```
kubectl version --client
```

### start minikube
```
minikube start
```

### minikube dashboard
```
minikube dashboard
```

### cluster info
```
kubectl cluster-info
```

### Deploy an Application 
*1. Create a simple deployment (e.g., Nginx):*

```
kubectl create deployment hello-world --image=nginx
```

*2. Expose the application as a service:*
```
kubectl expose deployment hello-world --type=NodePort --port=80
```

*3. Get the Service details:*
```
kubectl get services
```

*4. Access the service:*

```
minikube service hello-world
```


# Useful Minikube Commands
*Check Minikube status:*

```
minikube status
```

*Stop Minikube:*

```
minikube stop
```

*Delete Minikube:*

```
minikube delete
```

*View dashboard:*

```
minikube dashboard
```

#### settings.py

1. STATIC_URL: URL where the user can access your static files from in the browser. The default is `/static/`, which means your files will be available at http://127.0.0.1:8000/static/ in development mode -- e.g., http://127.0.0.1:8000/static/css/main.css.

2. STATIC_ROOT: The absolute path to the directory where your Django application will serve your static files from. When you run the `collectstatic` management command (more on this shortly), it will find all static files and copy them into this directory.

3. STATICFILES_DIRS: By default, static files are stored at the app-level at `<APP_NAME>/static/`. The collectstatic command will look for static files in those directories. You can also tell Django to look for static files in additional locations with `STATICFILES_DIRS`.

4. STORAGES: It specifies a way to configure different storage backends for managing files. Each storage backend can be given an alias, and there are two special aliases: `default` for managing files (with `FileSystemStorage` as the default storage engine) and `staticfiles` for managing static files (using `StaticFilesStorage` by default).

5. STATICFILES_FINDERS: This setting defines the file finder backends to be used to automatically find static files. By default, the           `FileSystemFinder` and `AppDirectoriesFinder` finders are used:

    > `FileSystemFinder` - uses the `STATICFILES_DIRS` setting to find files.

    > `AppDirectoriesFinder` - looks for files in a "static" folder in each Django app within the project.