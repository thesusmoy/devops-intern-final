# DevOps Intern Final Assessment

**Author:** Susmoy Debnath  
**Date:** 2025-11-26

## Project Description
This repository contains the final assessment for the DevOps Intern position. It demonstrates a complete DevOps workflow including:
- Linux Scripting
- Docker Containerization
- CI/CD with GitHub Actions
- Job Deployment with Nomad
- Monitoring with Grafana Loki

## Prerequisites

To fully run this project, you need the following tools installed.

### macOS Installation (via Homebrew)

**1. Docker**
```bash
brew install --cask docker
# Open Docker Desktop from Applications to start the daemon
open /Applications/Docker.app
```

**2. Nomad**
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/nomad
# Verify installation
nomad --version
```

## How to Run

### 1. Python Script
Run the simple python script:
```bash
python hello.py
```

### 2. Linux Script
Run the system info script:
```bash
./scripts/sysinfo.sh
```

### 3. Docker
Build and run the container:
```bash
docker build -t devops-intern-hello .
docker run devops-intern-hello
```

### 4. Nomad
Run the job (requires Nomad installed and running):
```bash
nomad job run nomad/hello.nomad
```

### 5. Monitoring
Refer to `monitoring/loki_setup.txt` for instructions on setting up and using Grafana Loki.

### 6. Extra Credit: MLFlow
Run the MLFlow experiment inside the container:
```bash
# Rebuild the image first
docker build -t devops-intern-hello .

# Run the experiment script
docker run devops-intern-hello python mlflow/experiment.py
```

