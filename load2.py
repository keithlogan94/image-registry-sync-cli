import requests
import json
import os
import time

local_repo_url = "http://localhost:5000"
local_repo_url_without_protocol = "localhost:5000"
ecr_registry_prefix = "403134974177.dkr.ecr.us-gov-west-1.amazonaws.com"

# login to docker
os.system(f"aws ecr get-login-password | docker login --username AWS --password-stdin {ecr_registry_prefix}")

# sleep for a little after logging in
time.sleep(5)

# get catalog of images from local repository
list_of_images_request_url = f"{local_repo_url}/v2/_catalog"
images_response = requests.get(list_of_images_request_url).content

# parse images into array
images_json = json.loads(images_response)['repositories']


# set list of images
list_of_images = images_json


# store all images
all_images = []

for image in list_of_images:

    # get image tags
    http_request_url = f"{local_repo_url}/v2/{image}/tags/list"


    response = requests.get(http_request_url)


    response_json_str = str(response.content.decode('utf-8'))
    obj = json.loads(response_json_str)


    image_name = obj["name"]

    for image_tag_it in obj["tags"]:

        image_with_tag = f"{image_name}:{image_tag_it}"
        image_pull_str = f"{local_repo_url_without_protocol}/{image_with_tag}"

        all_images.append(image_pull_str)





for print_image in all_images:
    # pull docker image from local registry
    os.system(f"docker pull {print_image}")
    time.sleep(1)
    new_image_tag = print_image.replace(local_repo_url_without_protocol, ecr_registry_prefix)

    tag_without_prefix = new_image_tag.replace(ecr_registry_prefix + '/', '').split(':')[0]
    print(f"tagging image {print_image} as {new_image_tag}")

    # retag it to ecr registry
    os.system(f"docker tag {print_image} {new_image_tag}")
    time.sleep(1)
    print("""

     NOW PUSHING

    

    """)



    os.system(f"aws ecr create-repository --repository-name {tag_without_prefix}")
    # push image to registry
    os.system(f"docker push {new_image_tag}")




    time.sleep(1)











