# Pneumonia Detection using Deep Learning

## Project Overview
This project aims to **detect pneumonia from chest X-ray images** using a deep learning model built with **TensorFlow and Keras**. The model achieves **90% accuracy** in classifying images as either normal or pneumonia. The project follows **best MLOps practices**, ensuring robustness and scalability through **DVC (Data Version Control)** for dataset management, **CI/CD pipelines** for automation, and **AWS EC2 for deployment**.

## Features
- **Deep Learning Model**: Built using **TensorFlow** and trained on labeled chest X-ray images.
- **High Accuracy**: Achieves **90% accuracy** in predicting pneumonia cases.
- **MLOps Integration**: Uses **DVC** for efficient dataset management and tracking.
- **CI/CD Pipeline**: Automates training, testing, and deployment.
- **AWS Deployment**: Hosted on **AWS EC2** with Docker integration.
- **Flask API**: Provides an endpoint to classify uploaded X-ray images.
- **Scalable and Reproducible**: Fully containerized with **Docker**.

---

## Tech Stack
- **Python** (Flask, TensorFlow, OpenCV, NumPy, Pandas, Matplotlib)
- **Machine Learning** (CNN, TensorFlow, Keras)
- **MLOps** (DVC, CI/CD with GitHub Actions)
- **Cloud Deployment** (AWS EC2, Docker)
- **Version Control** (Git, GitHub)

---

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/pneumonia-detection.git
cd pneumonia-detection
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project Locally
```bash
python app.py
```

The Flask API will be available at: **http://127.0.0.1:5000/**

---

## Data Version Control (DVC)
DVC is used to manage datasets efficiently without bloating Git repositories. It ensures **reproducibility, versioning, and tracking** of data and models.

### Initialize DVC
```bash
dvc init
git commit -m "Initialize DVC"
```

### Track the Dataset
```bash
dvc add data/
git add data.dvc .gitignore
git commit -m "Track dataset with DVC"
```

### Track the Model
```bash
dvc add models/
git add models.dvc .gitignore
git commit -m "Track model with DVC"
```

### Automate Workflow with DVC
```bash
dvc repro
```
This command ensures that all dependencies (data, preprocessing, training) are executed in order.

---

## CI/CD Pipeline (GitHub Actions)
This project integrates **CI/CD pipelines** to automate model training, testing, and deployment. The pipeline:
- **Runs unit tests** on every commit.
- **Triggers training** when dataset changes.
- **Deploys the model** to AWS EC2 after successful training.

### Steps to Configure:
1. **Set up a GitHub Repository** and push your project.
2. **Create a `.github/workflows/main.yml` file** for GitHub Actions.
3. **Add GitHub Secrets**:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_REGION`

---

## AWS Deployment (EC2, Docker)

### 1. Login to AWS Console & Create an EC2 Instance
- Select **Ubuntu** as the OS.
- Configure **Security Groups** (allow **port 8080** for API access).

### 2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

### 3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

### 4.Create EC2 machine (Ubuntu)

---
### 5.Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

### 6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

### 7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app

## Usage
- Upload an **X-ray image** to the Flask API.
- The model will predict whether the X-ray **shows pneumonia** or is **normal**.

---

## Conclusion
This project successfully implements **deep learning, MLOps, CI/CD, and cloud deployment** to detect pneumonia with high accuracy. The use of **DVC** ensures reproducibility, while **AWS EC2 and Docker** provide scalability for real-world deployment.
---

## Connect with Me  
For more details and professional connections, visit my **[LinkedIn Profile](https://www.linkedin.com/in/samarth-tikotkar-7532b0328/)**.  

Let me know if you want me to update the document with this! 🚀

## License
This project is licensed under the **MIT License**.

