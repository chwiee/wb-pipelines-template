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

deploy_name_value = input("Informe o valor para Orca.Project: ").strip()
kappa_build_value = input("Informe o valor para Orca.Token: ").strip()

group_payload = {
    "variables": {
        "Orca.Project": {
            "value": deploy_name_value,
            "isSecret": False
        },
        "Orca.Token": {
            "value": kappa_build_value,
            "isSecret": True
        }
    },
  "variableGroupProjectReferences": [
    {
      "name": "ORCA",
      "projectReference": {
        "id": f"{project_name}",
        "name": f"{project_name}"
      }
    }
  ],
  "name": "ORCA",
  "description": "ORCA variables - White Hat team"
}

response = requests.post(base_url, headers=headers, json=group_payload)

if response.status_code == 200:
    print(f"Grupo de variáveis criado com sucesso. ID: {response.json()['id']}")
else:
    print(f"Erro ao criar o grupo de variáveis. Código de Status: {response.status_code}")
    print("Detalhes:", response.text)
