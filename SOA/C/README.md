# Flask app
### Create and build docker container


docker build -t hello-world-app .


docker run -p 5000:5000 hello-world-app



### Push Image to dockerhub -------------
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname

docker tag hello-world-app mdnazmulhossain/hello-world-app:v1
docker push mdnazmulhossain/hello-world-app:v1



kubectl apply -f deployment.yaml
kubectl apply -f service.yaml








docker pull mdnazmulhossain/hello-world-app



docker tag hello-world-app <your-dockerhub-username>/hello-world-app:v1
