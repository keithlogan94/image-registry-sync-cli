from .list import get_list_of_images
import os
from ecr.ecr import login


class Image:

    def __init__(self, image_tag, local_repo_url_without_protocol, ecr_registry_prefix):
        """
        Image that represents both a local docker repo image, and a remote docker repo image
        :param image_tag: this tag is the tag from the local repo
        :param local_repo_url_without_protocol: local registry localhost:5000
        :param ecr_registry_prefix: remote registry 403134974177.dkr.ecr.us-gov-west-1.amazonaws.com
        """
        self.image_tag = image_tag
        self.remote_registry_tag = image_tag.replace(local_repo_url_without_protocol, ecr_registry_prefix)
        self.tag_without_prefix = self.remote_registry_tag.replace(ecr_registry_prefix + '/', '').split(':')[0]

    def get_pull_command(self, ctr_cli):
        return f"{ctr_cli} pull {self.remote_registry_tag}"

    def load_image_from_local_registry(self):
        """
        Pulls image from local registry
        :return: null
        """
        os.system(f"docker pull {self.image_tag}")

    def tag_from_local_to_remote_registry(self):
        """
        Tag image from local registry to remote
        :return:
        """
        os.system(f"docker tag {self.image_tag} {self.remote_registry_tag}")

    def push_to_remote(self, create_repo=True):
        """
        Push image to remote registry
        :param create_repo:
        :return:
        """
        login()
        if create_repo:
            os.system(f"aws ecr create-repository --repository-name {self.tag_without_prefix}")
        # push image to registry
        os.system(f"docker push {self.remote_registry_tag}")

    @staticmethod
    def load_list_of_images(local_repo_url_without_protocol, ecr_registry_prefix):
        images = []
        all_images_tags = get_list_of_images()

        for image_tag in all_images_tags:
            image = Image(image_tag, local_repo_url_without_protocol, ecr_registry_prefix)
            images.append(image)

        return images

    @staticmethod
    def push_all_images_to_remote(local_repo_url_without_protocol, ecr_registry_prefix):
        images = Image.load_list_of_images(local_repo_url_without_protocol, ecr_registry_prefix)

        for image in images:
            image.load_image_from_local_registry()
            image.push_to_remote()

    @staticmethod
    def create_pull_image_bash(local_repo_url_without_protocol, ecr_registry_prefix, ctr_cli="docker"):
        images = Image.load_list_of_images(local_repo_url_without_protocol, ecr_registry_prefix)
        file = open("pull.sh", "w+")
        for image in images:
            file.write(image.get_pull_command(ctr_cli) + "\n")
        file.close()
        print("pull.sh created")


