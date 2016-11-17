#!/usr/bin/python
# arquivo: DeployTool.py

import yaml
import argparse
from Modulos.Docker import Docker

class DeployTool:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i",help="Define o arquivo de deploy")

    def read_yaml(self,arquivo):
        with open(arquivo, "r") as f:
            self.arquivo = yaml.load(f.read())        

    def get_args(self):
        return self.parser.parse_args()

    def main(self):
        d = Docker()
        print "Criando container: ",self.arquivo.get("name")
        container = d.criar_container(self.arquivo.get("name"))
        d.iniciar_container(container)
        print "Clonando repositorio: ",self.arquivo.get("repo")
        print "Instalando aplicacao..."
        for c in self.arquivo.get("commands"):
            print "Executando: ",c
            saida = d.executar_comando(container,c)
            print saida
        print "Maquina provisionada no IP: ",d.inspecionar_container(container).get("NetworkSettings").get("IPAddress")



if __name__ == '__main__':
    d = DeployTool()
    args = d.get_args()
    d.read_yaml(args.i)
    d.main()




