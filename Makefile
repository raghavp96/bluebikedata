start:
	python container_manager.py start 

stop:
	python container_manager.py stop

restart:
	python container_manager.py restart

gcp-deploy:
	echo -e "Building all Docker images....\n"
	python container_manager.py build 
	echo -e "Pushing latest images to GKE Container Registry...\n"
	docker push gcr.io/cs3200-215502/auth_svc:v1
	docker push gcr.io/cs3200-215502/api_svc:v1
	docker push gcr.io/cs3200-215502/live_data_svc:v1
	docker push gcr.io/cs3200-215502/data_svc:v1
	