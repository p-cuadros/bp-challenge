# Devops Challenge

- CI with Github Actions, include unit testing and static code analysis.
- CD with Github Actions and Kubernetes manifest file, previusly, it's necesary provisioning the infraestructure, [here the steps.](manifests/provision_infra.md)

First generate token in: http://20.76.254.20/get_token

EndPoint URL: http://20.76.254.20/

Token: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c

The APIKey must be included in HTTP Headers
In our side, we will use this command to test your endPoint

```
curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "X-JWT-KWY: ${JWT}" \
-H "Content-Type: application/json" \
-d '{ "message" : "This is a test", "to": "Juan Perez", "from": "Rita Asturia", "timeToLifeSec" : 45 }' \
http://20.76.254.20/DevOps
```

