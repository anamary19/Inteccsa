#aquí se configuran algunos datos necesarios para la configuración del paquete distribuible

from setuptools import setup, find_packages

#configuración básica de un paquete distribuible

setup(
    name = "paquetetnueve",
    version = "0.1",
    description= "paquete distribuible de prueba para tema nueve",
    author="jorge",
    author_email= "mail.author@mail.com",
    url="https://www.jorgeauthor.com",
    packages=["paquete", "paquete.subpaqueteA"],
    scripts=[]
)