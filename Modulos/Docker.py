#!/usr/bin/python

from docker import Client
import time

class Docker:
    def __init__(self):
        self.client = Client(base_url="tcp://192.168.0.2:2376")

    def listar_containers(self):
        for c in self.client.containers(all=True):
            print c

    def criar_container(self,nome="novo",imagem="ubuntu",comando="/bin/bash"):
        container = self.client.create_container(image=imagem,
                           command=comando,
                           name=nome,
                           stdin_open=True,
                           tty=True,
                           detach=True)
        return container

    def iniciar_container(self,id):
        self.client.start(container=id)
        print "Container iniciado!"

    def parar_container(self,id):
        self.client.stop(container=id)
        print "Container parado!"

    def remove_container(self,id):
        self.client.stop(container=id)
        self.client.remove_container(container=id)
        print "Container removido!"

    def executar_comando(self,id,comando):
        exec_id = self.client.exec_create(container=id,cmd=comando)
        resultado = self.client.exec_start(exec_id)
        return resultado

    def inspecionar_container(self,id):
        container = self.client.inspect_container(container=id)
        return container

if __name__ == '__main__':
    d = Docker()
    container = d.criar_container("novo3")
    d.iniciar_container(container)
    #d.listar_containers()
    ip = d.inspecionar_container(container)
    print "IP: ",ip.get("NetworkSettings").get("IPAddress")
    print d.executar_comando(container,"apt-get update")
    time.sleep(10)
    d.parar_container(container)
    d.remove_container(container)






