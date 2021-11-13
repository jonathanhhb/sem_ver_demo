import setuptools
from setuptools.extension import Extension
import module_b

with open("README.md", "r") as fh:
    long_description = fh.read()
    ext_name = "module_b"

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split("\n")

setuptools.setup(
    name=ext_name,
    version=module_b.__version__,
    author="Jonathan Bloedow",
    author_email="jbloedow@idmod.org",
    description="Module A (app-level)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonathanhhb/sem_ver_demo",
    packages=setuptools.find_packages(exclude=[""]),
    include_package_data=True,
    setup_requires=['wheel'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
