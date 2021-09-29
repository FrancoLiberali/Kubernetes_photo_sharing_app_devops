docker run --link mongo-service --link photographer-service -v $(pwd):/app -p 90:80 --name photo-service photo /start-reload.sh
