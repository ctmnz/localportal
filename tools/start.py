import docker



def start_my_localportal():
    client = docker.from_env()
    client.containers.run("ctmnz/localportal", command=None, detach=True, ports={'8080/tcp': 8088}, name="pydocker")

start_my_localportal()





