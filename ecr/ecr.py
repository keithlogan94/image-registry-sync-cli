import os


def login(ecr_registry_prefix):
    # login to docker
    os.system(f"aws ecr get-login-password | docker login --username AWS --password-stdin {ecr_registry_prefix}")
