from setuptools import setup, find_packages

setup(
    name='AnaPachonT9',
    version='1.0.0',
    author='Ana Pachon',
    author_email='anapachon@mail.com',
    description='Paquete con funciones de cadenas y conversiones',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https:anamaria.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.6',
)
