# Provisioning Kubernetes Cluster in Azure (AKS).

1. Go to the Azure Portal: https://ms.portal.azure.com/#home and open the Cloud Shell or use Azure CLI.
2. Create a resource group
    ```
    az group create --name <RESOURCEGROUPNAME> --location westeurope
    ```
3. Create an Azure Container Registry (ACR)
    ```
    az acr create --resource-group <RESOURCEGROUPNAME> --name <ACRNAME> --sku Basic
    ```
4. Get username & password from ACR
    ```
    az acr update -n <ACRNAME> --admin-enabled true
    az acr credential show -n <ACRNAME>
    ```
5. In GitHub, browse to your repository, select Settings > Secrets > Add a new secret and add the username and password from the last step in the following secret variables: REGISTRY_USERNAME REGISTRY_PASSWORD
6. Create an AKS cluster (you have to wait a few minutes)
    ```
    az aks create \
        --resource-group <RESOURCEGROUPNAME> \
        --name <AKSNAME> \
        --node-count 2 \
        --generate-ssh-keys \
        --attach-acr <ACRNAME>
    ```
7. Create a Service Principal. You can create a service principal by using the az ad sp create-for-rbac command.
    ```
    az ad sp create-for-rbac --name <APPNAME> --role contributor --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP> --sdk-auth
    ```
8. Obtain the <SUBSCRIPTION_ID> by using > az account list. Copy this JSON object, which you can use to authenticate from GitHub. Add it to the following secret variable: AZURE_CREDENTIALS
