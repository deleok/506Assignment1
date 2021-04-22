# clone the container based on another one (python:3.9-slim-buster)
FROM python:3.9-slim-buster
RUN pip3 install Flask
# define the current directory in the container
WORKDIR /app
# copy everything in the current directory of the host machine (first dot)
# to the current directory inside the docker container /app (second dot)
COPY . .
CMD ["python3", "app.py"]