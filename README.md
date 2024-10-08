## Auto-Grader Cloud App

I developed a scalable cloud-based auto-grader system using Docker and AWS Elastic Beanstalk. The project involved several steps:

1. **Docker**: Set up a t2.large Ubuntu server on AWS, installed Docker, and completed an in-depth tutorial to understand containerization and Docker’s functionalities.
2. **Web Server Development**: Created a web server application using Python and Flask. The application allows users to upload a C++ program, which is then auto-graded. The system compiles the uploaded program, executes it, and compares the output to expected results, providing real-time feedback and grade.
3. **Docker Integration**: Transformed the web server application into a Docker container.
4. **AWS Elastic Beanstalk Deployment**: Deployed the Docker container to AWS Elastic Beanstalk.

### Skills Gained:
• Proficiency in Docker and containerization.
• Experience with AWS services, (EC2 and Elastic Beanstalk.)
• Hands-on development with Python, Flask, and web server management.
• Practical understanding of cloud-based application deployment and scalability.

<img width="468" alt="image" src="https://github.com/user-attachments/assets/49656217-b009-40cd-a48a-06d0a34e7f73">
<img width="468" alt="image" src="https://github.com/user-attachments/assets/2c768287-4fdd-40c4-93e3-a50c9b3915e8">
<img width="468" alt="image" src="https://github.com/user-attachments/assets/d84c3bf3-03ed-4db0-9622-55b28b5c3bfe">
<img width="468" alt="image" src="https://github.com/user-attachments/assets/6b0e2779-e730-4a79-9cce-5a10daad5a60">
<img width="468" alt="image" src="https://github.com/user-attachments/assets/d1800451-1cd4-4794-ab11-c866e0e959ad">
<img width="468" alt="image" src="https://github.com/user-attachments/assets/b6cb62ff-90dc-49c4-be9d-2769a2e41296">

## Compose Sample Application

### Use with Docker Development Environments

You can open this sample in the Dev Environments feature of Docker Desktop version 4.12 or later.

[Open in Docker Dev Environments <img src="../open_in_new.svg" alt="Open in Docker Dev Environments" align="top"/>](https://open.docker.com/dashboard/dev-envs?url=https://github.com/docker/awesome-compose/tree/master/flask)

### Python/Flask Application

Project structure:
```
.
├── compose.yaml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py
```

[_compose.yaml_](compose.yaml)
```
services: 
  web: 
    build:
     context: app
     target: builder
    ports: 
      - '8000:8000'
```

## Deploy with Docker Compose
```
$ docker compose up -d
[+] Building 1.1s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                       0.0s
    ...                                                                                                                                         0.0s
 => => naming to docker.io/library/flask_web                                                                                                                                                                                               0.0s
[+] Running 2/2
 ⠿ Network flask_default  Created                                                                                                                                                                                                          0.0s
 ⠿ Container flask-web-1  Started
```

## Expected Result

Listing containers must show one container running and the port mapping as below:
```
$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
flask-web-1         "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp
```

After the application starts, navigate to `http://localhost:8000` in your web browser or run:
```
$ curl localhost:8000
Hello World!
```

Stop and remove the containers
```
$ docker compose down
```
