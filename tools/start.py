import docker
import sys

app_container_name="pylocalportal"



def start_my_localportal():
    client = docker.from_env()

    running_containers = client.containers.list()
    for i in running_containers:
        if i.name == app_container_name:
            sys.exit("The container is currnetly running! Aborting the operation.")
		

    client.containers.run("ctmnz/localportal", command=None, detach=True, ports={'8080/tcp': 8088}, name=app_container_name)

start_my_localportal()





