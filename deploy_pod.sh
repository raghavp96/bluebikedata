# Deploy to GKE
echo "Getting Pods..."
echo ""

kubectl get pods
echo ""

# kubectl get pods
# echo ""

# kubectl run auth-svc --image=gcr.io/cs3200-215502/auth-svc:v1 --port 8000
# echo "Sleeping a bit..."
# sleep 5


kubectl run api-svc --image=gcr.io/cs3200-215502/api-svc:v1 --port 8001
echo "Sleeping a bit..."
sleep 5



# echo "Sleeping a bit..."
# sleep 5
# kubectl run live-data-svc --image=gcr.io/cs3200-215502/live-data-svc:v1 --port 8002
# echo "Sleeping a bit..."
# sleep 5
# kubectl run data-svc --image=gcr.io/cs3200-215502/data-svc:v1 --port 8003
# echo "Sleeping a bit..."
# sleep 5

# kubectl get pods
# echo ""

# Create kubernetes cluster with only one node
# Change urls in each Dockerfile to refer to that node's ip and port in Docker file
# Deploy each container as a Pod and expose its port

# kubectl expose deployment auth-svc --type=LoadBalancer --port 80 --target-port 8080
kubectl expose deployment api-svc --type=LoadBalancer --port 80 --target-port 8080
# kubectl expose deployment data-svc --type=LoadBalancer --port 80 --target-port 8080
# kubectl expose deployment live-data-svc --type=LoadBalancer --port 80 --target-port 8080