docker run --name mongo-service -d mongo
docker run --link mongo-service -v $(pwd):/app -p 80:80 --name photographer-service photographer /start-reload.sh
