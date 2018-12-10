Deploy Directions

In `gcp` directory:

```
cd gcr && sudo ./deploy_images.sh
```

to deploy all the images to GCR. Then:

```
cd ../gke
sudo kubectl get deployments

```

Want to deploy the api service again?

```
sudo kubectl delete deployment bluebikedata-api-server
cd api
sudo kubectl create -f api-server-deployment.yml
```

We don't need to deploy the k8s Service again. It's already running - we just redeploy and it picks it up.


Want to deploy the nginx service again?

```
sudo kubectl delete deployment nginx-svc
cd api
sudo kubectl create -f nginx-deployment.yml
```

We don't need to deploy the k8s Service again. It's already running - we just redeploy and it picks it up.