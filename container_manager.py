import json
import os
import subprocess
import sys
import docker

# cloned and adapted from https://github.com/raghavp96/dockernetes

docker_client = docker.from_env()

with open('config.json') as json_file:  
    data = json.load(json_file)

dir_path = os.path.dirname(os.path.realpath(__file__))

def build():
    __build_containers()

def start():
    __build_containers()
    __create_network()
    __run()

def stop():
    __stop_and_remove_containers()
    __remove_network()

def restart():
    stop()
    start()

def __build_containers():
    for container in data["Network"]["Containers"]:
        docker_client.images.build(path=dir_path +'/' + container["Folder"], tag=container["ImageName"], rm=True)
    
def __create_network():
    docker_client.networks.create(data["Network"]["Name"], driver="bridge")

def __run():
    for container in data["Network"]["Containers"]:
        docker_client.containers.run(name=container["ContainerName"], image=container["ImageName"], detach=True, network=data["Network"]["Name"], ports={container["Port"] + '/tcp': container["ExternalPort"]}, publish_all_ports=True)        

def __stop_and_remove_containers():
    for container in data["Network"]["Containers"]:
        s = subprocess.call(["docker", "stop", container["ContainerName"]])
        print(s)
        s = subprocess.call(["docker", "container", "rm", container["ContainerName"]])
        print(s)

def __remove_network():
    s = subprocess.call(["docker", "network", "rm", data["Network"]["Name"]])
    print(s)

functions = {
    'build' : build,
    'start' : start,
    'stop' : stop,
    'restart' : restart
}

if __name__ == '__main__':
    func = functions[sys.argv[1]]
    sys.exit(func())