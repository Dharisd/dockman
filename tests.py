from DockerClient import  DockerHelper


docker = DockerHelper()

containers = docker.list_containers()
for x in containers:
    print(x)
    print("\n")

container = containers[1]["id"]

logs = docker.get_logs(container)
print(logs)