### Terraform section:

Create infrastructure:
```
terraform apply
# While on the TF/ directory collect the following information:
AWS_ACCOUNT_ID=$(terraform output -raw registry_id)
REGION=$(terraform output -raw region)
REPOSITORY=$(terraform output -raw repository_url)
CLUSTER_NAME=$(terraform output -raw cluster_name)
```

Create the Docker image:
```
# Clone the repository, cd into API/ and build the Docker image.
cd ../API/
IMAGE_NAME=myimage # Maybe '590184000874.dkr.ecr.us-east-1.amazonaws.com/jpmc-ecr:latest' instead.
docker build -t $IMAGE_NAME .
```

### Docker section:
Login to the registry (this step is necesary):
```
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
```

Now tag it?:
```
VERSION=latest
docker tag $IMAGE_NAME:$VERSION $REPOSITORY
```

Now push it:
```
docker push $REPOSITORY
```

### Kubernetes section:
Configure `kubectl` to use the recently created Kubernetes cluster:
```
aws eks --region $REGION update-kubeconfig --name $CLUSTER_NAME
```

## Deploy container to Kubernetes cluster:

A bit counterintuitive, but first create the service:
```
kubectl create service loadbalancer fast-api --tcp=80:80
```

Only after creating the service you should create the deployment:
```
kubectl create deployment fast-api --image=$REPOSITORY --replicas=3
# May be useful for testing, but should not be needed:
kubectl port-forward <the_name_of_a_pod> 8080:80
# To list the pods: `kubectl get pods`
```

## Check and verify:
```
DNS_NAME=$(kubectl get service | grep ^fast-api | awk '{ print $4 }')
curl $DNS_NAME


## REFERENCES:

Using Amazon ERC with the AWS CLI:
https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html

Create a Kubernetes deployment:
https://www.loginradius.com/blog/engineering/rest-api-kubernetes/#3-deploy

Deploy a simple Python & FastAPI application to Kubernetes:
https://www.youtube.com/watch?v=XltFOyGanYE