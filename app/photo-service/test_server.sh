docker run --link mongo-service-test --link tags-service-test -v $(pwd):/app -w /app photoapptest pytest -p no:warnings
