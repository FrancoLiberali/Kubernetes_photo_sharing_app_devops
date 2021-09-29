docker run --link mongo-service-test -v $(pwd):/app -w /app photoapptest pytest -p no:warnings
