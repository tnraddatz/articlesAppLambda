Followed this guide https://medium.com/better-programming/set-up-a-ci-cd-pipeline-for-aws-lambda-with-github-actions-and-serverless-in-under-5-minutes-fd070da9d143

Create the app

```
serverless create --template aws-python3 --path myApp
```

update handler.py 

```
serverless plugin install -n serverless-python-requirements
```

copy this files `serverless.yaml` 

copy this files `.gitignore`

create `.github/workflows/deploy-aws-lambda.yaml` and change the `name`

add `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

create `requirements.txt` and put dependencies there