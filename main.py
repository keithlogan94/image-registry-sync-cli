import argparse
from images.image import Image

# local_repo_url = "http://localhost:5000"
# local_repo_url_without_protocol = "localhost:5000"
# ecr_registry_prefix = "403134974177.dkr.ecr.us-gov-west-1.amazonaws.com"


def main():
    parser = argparse.ArgumentParser(description='Local Docker registry pull and push cli')
    parser.add_argument('--local-registry-url-with-protocol',
                        required=True,
                        help='url to local docker registry example: http://localhost:5000')

    parser.add_argument('--local-registry-url-without-protocol',
                        required=True,
                        help='url to local docker registry example: http://localhost:5000')

    parser.add_argument('--remote-registry',
                        required=True,
                        help='remote docker registry example: 403134974177.dkr.ecr.us-gov-west-1.amazonaws.com')

    parser.add_argument('--action',
                        required=True,
                        help='action: transfer, build_pull_script')

    parser.add_argument('--ctr-cli',
                        required=True,
                        help='ctr-cli: docker, crictl')
    args = parser.parse_args()

    if args.action == "transfer":
        Image.push_all_images_to_remote(args.local_registry_url_without_protocol,
                                  args.remote_registry)
    elif args.action == "build_pull_script":
        Image.create_pull_image_bash(args.local_registry_url_without_protocol,
                                  args.remote_registry,
                                     args.cri_ctl)
    else:
        parser.error("args.action not found")


if __name__ == "__main__":
    main()

