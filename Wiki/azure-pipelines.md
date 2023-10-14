# Azure Pipelines DOC

## What is this

This repo's got the yamls for pipelines that are all about Azure DevOps for CI and CD, and it's just using the Yaml Pipelines features. No Task Groups or artifact-making here, buddy! 😉

## How do this work

This repo's like a BFF(user friendly) for devs. Just with 2 files, you've got a standard pipeline, whether you're using stuff the infra, security, and automation crews have already tested or not. So not only do we keep a full CI & CD game going, but we can also drop some fresh updates for all the squads involved! 🚀

# File Structure Explanation

- **Stages**: A folder holding all the Pipeline stages. Inside, there's a file named `model.yaml`. This file outlines all the steps the pipeline will run, based on the variables filled in the `azure-pipelines.yaml` file.

- **Automacores**: This folder contains all the automations we can use to set up the teams' pipelines, which includes:
   - `orca.py`: Generates the variable group for ORCA (commonly used by the Security team).
   - `common-vars`: Generates a variable group with the pipeline's default variables (see the pipeline variable table). This script can be used instead of populating all the pipelines with the `var.yaml` file containing repeated values.

## Initial steps
 
To get this repo up and running, just follow these steps:

1. Inside the repo, whip up 2 files named `azure-pipelines.yaml` and `vars.yaml`.
2. Copy the content from the 2 original files (found in this repo) into the ones you just made in your app's repo.
3. In the azure-pipelines.yaml, fill in the deets of the actions you wanna run in your pipeline (check out the examples in the next sections). If you're feeling lost, peep the table here to get what each thing means and what you gotta put in.
4. Now, fill out the vars.yaml with the right info to make your pipeline run smooth (again, examples below). If it's all Greek to you, there's a table here to break it down.

##Setting up your pipeline

1. With everything set in your repo, head over to "**Pipelines**" > "**Pipelines**" > "**Create new Pipeline**" > "**Azure Repos**" > **Find your repo** > "**Use exists yaml file**" > Pick the "**azure-pipelines.yaml**" from the branch you want.
2. Hit "**Run**".

## Tables

### Pipelines table 

| Term  | Type     | Description                                                                                                                                                                                                                                           |
|-------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ORCA  | Boolean  | System used by the security team to check if the app and/or container has vulnerabilities.                                                                                                                                                             |
| SONAR | Boolean  | Code quality system.                                                                                                                                                                                                                                  |
| BUILD | String   | Sets the app's build type. Options are: <br /> 1. docker: Using Dockerfile <br /> 2. Kaniko: Uses Kaniko feature to build within the EKS cluster (also uses Dockerfile). <br /> 3. dotnet: For building inside a physical EC2 instance (no Dockerfile).                      |
| DEPLOY| String   | Sets the deploy type. Options are: <br />1. k8s: Kubernetes rolling update deploy <br />2. canary: Canary deploy where a certain % of new PODs with the new version are created, keeping the rest on the old version. <br />3. IIS: Deploy for legacy environments that still use IIS to serve the app to the Cloud. <br />4. Lambda: Lambda deploy. |

**NOTE:** To use ORCA, you need to set up a library whith the script in `automacao` path:


--------------------------------

### Variables table
| Variable                | Type   | Description                                                                                                                                    |
|-------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------|
| AWS.Ecr.Account         | String | Provide the account ID where the image will be stored.                                                                                         |
| AWS.Ecr.Account.Name    | String | Provide the account name where the image will be stored.                                                                                         |
| AWS.Ecr.Region          | String | Specify the region where this repository's ECR will be created.                                                                                |
| AWS.Account             | String | List all the accounts that will have access to this repository. Example format: '123456789,987654321,098234512,123495761'. Separate accounts with a comma(,).  |
| Build.PoolName          | String | Enter the BUILD POOL name for your environment (usually we use XXXXXXXXXXXXX).                                                                 |
| Deploy.ClusterName      | String | Indicate the prefixes of your cluster. For example, if your cluster is registered as xpto-eks-prod in your project's Azure DevOps service connections, use only 'xpto-eks'.     |
| Deploy.Namespace        | String | Specify the namespace used to create the resource in Kubernetes (if it's Kubernetes) otherwise it will be created in Default.                      |
| Deploy.PoolName         | String | Specify the Pool name where the deployment Agents are (remember there should be 1 agent per environment). Check the Wiki 'Multi Environment Azure Agents' for more info.       |
| CMFAI.Config.Item       | string | Provide the name of the config item registered in EP.                                                                                          |
| Deploy.Files            | string | path where the Kubernetes manifest files are located                                                                                          |




# *BOOM! Your pipeline's good to go! :)*

## Maintance 

Wallace Gentil - 09/10/2023 - Add this file :)

# Tks :)