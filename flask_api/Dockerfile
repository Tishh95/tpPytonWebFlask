# Set the base image to Ubuntu
FROM python:3.8-slim-buster
 WORKDIR /work
 RUN python3 -m pip install --upgrade pip
 COPY . .
 CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
