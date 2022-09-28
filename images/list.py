import requests
import json


def get_list_of_images(local_repo_url="http://localhost:5000", local_repo_url_without_protocol="localhost:5000"):
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

    return all_images



