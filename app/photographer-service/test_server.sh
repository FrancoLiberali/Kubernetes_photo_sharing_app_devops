docker run --name mongo-service-test -d mongo
docker run --link mongo-service-test -v $(pwd):/app -w  /app photoapptest pytest -p no:warnings
