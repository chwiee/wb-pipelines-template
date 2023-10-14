import requests
import base64

organization_name = input("Informe o nome da organização no Azure DevOps: ")
project_name = input("Informe o nome do projeto no Azure DevOps: ")
personal_access_token = input("Informe o seu Personal Access Token (PAT): ")

auth_string = ':' + personal_access_token
base64_bytes = base64.b64encode(auth_string.encode('utf-8'))
headers = {
    'Authorization': 'Basic ' + base64_bytes.decode('utf-8'),
    'Content-Type': 'application/json'
}

base_url = f'https://dev.azure.com/{organization_name}/{project_name}/_apis/distributedtask/variablegroups?api-version=6.1-preview.2'

ecr_account_id          = input("Informe o ID da conta AWS onde as imagens dos containers serão criadas: ").strip()
ecr_account_name        = input("Informe o nome da conta AWS onde as imagens dos containers serão criadas: ").strip()
ecr_region              = input("Informe a região dos ECRs: ").strip()
build_pool_name         = input("Informe o nome do Pool que será usado para Build: ").strip()
deploy_pool_name        = input("Informe o nome do Pool que será usado para Deploy: ").strip()
cluster_name            = input("Informe o nome do Cluster: ").strip()
deploy_files            = input("Informe o caminho onde os arquivos de manifestos Kubernetes estão: ").strip()

group_payload = {
    "variables": {
        "AWS.ECR.Account": {
            "value": ecr_account_id,
            "isSecret": False
        },        
        "AWS.ECR.Account.Name": {
            "value": ecr_account_name,
            "isSecret": False
        },
        "AWS.ECR.Region": {
            "value": ecr_region,
            "isSecret": False
        },
        "Build.PoolName": {
            "value": build_pool_name,
            "isSecret": False
        },
        "Deploy.PoolName": {
            "value": deploy_pool_name,
            "isSecret": False
        },
        "Deploy.ClusterName": {
            "value": cluster_name,
            "isSecret": False
        },
        "Deploy.Files": {
            "value": deploy_files,
            "isSecret": False
        },
    },
    "variableGroupProjectReferences": [
    {
        "name": f"{project_name}-common",
        "projectReference": {
            "id": f"{project_name}",
            "name": f"{project_name}"
        }
    }
    ],
    "name": f"{project_name}-common",
    "description": "Common variables to use in Pipelines"
}

response = requests.post(base_url, headers=headers, json=group_payload)

if response.status_code == 200:
    print(f"Grupo de variáveis criado com sucesso. ID: {response.json()['id']}")
else:
    print(f"Erro ao criar o grupo de variáveis. Código de Status: {response.status_code}")
    print("Detalhes:", response.text)
