# Workshop: Installing Docker

In this hands-on workshop, we'll guide you through the process of installing Docker.

## Installing Docker

### 1. Update the Package Database
Before installing Docker, it's a good practice to update the package database:
```bash
sudo yum update -y
```
### 2. Install Docker
To install Docker, use the following command:
```
sudo yum install docker -y
```
### 3. Start the Docker Service
Once the installation is complete, start the Docker service:
```bash
sudo service docker start
```
### 4. Verify Docker Installation
To ensure Docker is correctly installed and running, run the following command:
```bash
docker --version
```
You should see the Docker version printed, indicating a successful installation.

## Conclusion

Congratulations! You've successfully installed Docker. Now you're ready to pull and run containers on your environment.
