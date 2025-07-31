# Chatbot DevOps Pipeline

A modern CI/CD & GitOps demo project for a FastAPI-based chatbot, deployed with Kubernetes, ArgoCD, Istio, and best DevOps patterns.

## Running locally

1. Install requirements:
    ```
    pip install fastapi[all] uvicorn
    ```
2. Run the API:
    ```
    uvicorn src.api.main:app --reload
    ```
3. Test the health endpoint:
    - http://localhost:8000/

## CI/CD

- Automated build, lint, and test run for every PR/push using [GitHub Actions](.github/workflows/ci.yml)
