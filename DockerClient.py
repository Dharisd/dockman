import docker

class DockerHelper:

    def __init__(self):
        self.client = docker.from_env()

    def filter_container_object(self,container):
        filtered = {
            "id":container.attrs["Id"],
            "name":container.attrs["Name"],
            "created":container.attrs["Created"],
            "status":container.attrs["State"]["Status"],
            "started":container.attrs["State"]["StartedAt"],
            "finished":container.attrs["State"]["FinishedAt"],
            "args":container.attrs["Args"],    
            "port_bindings":container.attrs["HostConfig"]["PortBindings"],
            "mounts":container.attrs["HostConfig"]["Binds"]
        }

        return filtered


    """list all running containers and return detail of each container"""
    def list_containers(self):
        containers = self.client.containers.list()
        all_containers = []

        for container in containers:
            filtered = self.filter_container_object(container)
            all_containers.append(filtered)

        return all_containers
    
    """return logs given container id"""
    def get_logs(self,container_id):
        container = self.client.containers.get(container_id)
        logs = container.logs()

        return logs

    """runs a container given a image name"""
    def run_container(self,container_name):
        container = self.client.containers.run(container_name,detach=True)
        return container

    """runs a container given container id"""
    def start_container(self,container_id):
        container = self.client.containers.get(container_id)
        attempt_run  = container.start()
        return filter_container_object(attempt_run)        


    """stop a container given container id"""
    def stop_container(self,container_id):
        container = self.client.containers.get(container_id)
        attempt_stop  = container.stop()
        return filter_container_object(attempt_stop)  


    """restart a container given container id"""
    def restart_container(self,container_id):
        container = self.client.containers.get(container_id)
        action  = container.restart()
        return filter_container_object(action)  

    """restart a container given container id"""
    def kill_container(self,container_id):
        container = self.client.containers.get(container_id)
        action  = container.restart()
        return filter_container_object(action)  


    """pause a container given container id"""
    def pause_container(self,container_id):
        container = self.client.containers.get(container_id)
        action  = container.pause()
        return filter_container_object(action)  

        