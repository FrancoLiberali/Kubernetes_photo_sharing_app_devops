-H 'accept: application/json' \
  -H 'Content-Type: application/json' \

curl --insecure https://apim.example.com/gateway/photographer/photographers \
-X POST \
-H 'X-Gravitee-Api-Key: 9a6ffb0a-c474-4d71-9e7b-259bb3672615' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"display_name": "rdoisneau", "first_name": "robert", "last_name": "doineau", "interests": ["street", "portrait"]}'

curl --insecure https://apim.example.com/gateway/photographer/gallery/rdoisneau \
-X POST \
-H 'X-Gravitee-Api-Key: 9a6ffb0a-c474-4d71-9e7b-259bb3672615' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'file=@Screenshot from 2021-09-21 18-35-32.png;type=image/png'