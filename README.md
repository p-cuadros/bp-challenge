# devops-challenge

DevOps Technical Assessment

First generate token in: http://localhost:5000/get_token

EndPoint URL: http://localhost:5000

Token: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c

The APIKey must be included in HTTP Headers
In our side, we will use this command to test your endPoint
curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "X-JWT-KWY: ${JWT}" \
-H "Content-Type: application/json" \
-d '{ "message" : "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec" : 45 }' \
http://localhost:5000/DevOps
