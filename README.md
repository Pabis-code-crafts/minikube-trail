# Jenkins Pipeline for Docker and Kubernetes

This project uses Jenkins to build a Docker image, push it to Docker Hub, and deploy it to a Kubernetes cluster.

## Requirements

- Jenkins
- Docker
- Kubernetes
- Docker Hub account

## Pipeline Steps

1. **Build Docker Image**
    - Builds a Docker image using the source code.

2. **Push Docker Image**
    - Pushes the Docker image to Docker Hub.

3. **Deploy to Kubernetes**
    - Deploys the Docker image to a Kubernetes cluster using `deployment.yaml` and `service.yaml`.

## Files

- `Jenkinsfile`: The pipeline script.
- `deployment.yaml`: Kubernetes deployment configuration.
- `service.yaml`: Kubernetes service configuration.

## Usage

1. Ensure Jenkins, Docker, and Kubernetes are set up.
2. Configure Jenkins with your Docker Hub credentials.
3. Add the `Jenkinsfile`, `deployment.yaml`, and `service.yaml` to your repository.
4. Run the pipeline in Jenkins.

The pipeline will automatically build, push, and deploy your Docker image.
