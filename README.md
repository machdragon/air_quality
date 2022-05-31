# air_quality
 
air quality api dockerized python flask deployment using kubernetes minikube running every 15 minutes on cron job

1. Request an API token from https://aqicn.org/data-platform/token/
2. Deploy script to retrieve air quality data from api passing in /city/token in Flask web app fields
3. Create dockerfile and build docker image to deploy to minikube
4. configure helm kube cronjob and deploy to run every 15 min  

In Powershell  
minikube start  
& minikube -p minikube docker-env --shell powershell | Invoke-Expression  
docker build -t airquality .   
minikube image load airquality .  
kubectl create -f cron-job.yaml  

Verify working locally  
docker run --publish 8000:5000 airquality  
curl localhost:8000/seattle/token  
