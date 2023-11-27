#  🔗[password-manager](http://18.117.240.172:8000/)
# django-docker

This is a production-ready setup for running Django on Docker. It has sensible defaults for security, scaling, and workflow. It's a robust and simple way to run Django projects on production servers.

## Quick start

    $ cp config.ini.sample config.ini # add your server details here
    $ fab deploy_production

That's it—you now have a fully Dockerized Django project running on a production server. Read below for details on configuring the project and managing the development workflow.

## Installation

First, [install Docker](https://docs.docker.com/installation/). If you're new to Docker, you might also want to check out the [Hello, world! tutorial](https://docs.docker.com/userguide/dockerizing/).

Next, clone this repo:

    $ https://github.com/loopassembly/password-manager.git
    $ cd password-manager

(Mac users should clone it to a directory under `/Users` because of a [Docker bug](https://blog.docker.com/2014/10/docker-1-3-signed-images-process-injection-security-options-mac-shared-directories/) involving Mac shared directories.)

You can also fork this repo or pull it as  image from Docker Hub as [`morninj/django-docker`](https://hub.docker.com/r/morninj/django-docker/).


Update the `origin` to point to your own Git repo:

    $ git remote set-url origin https://github.com/loopassembly/password-manager.git


## Configure the project

Project settings live in `config.ini`. It contains sensitive data, so it's excluded in `.gitignore` and `.dockerignore`. Copy `config.ini.sample` to `config.ini`:

    $ cp config.ini.sample config.ini

Edit `config.ini`. At a minimum, change these settings:

* `DOCKER_IMAGE_NAME`: change to `<yourname>/some-image-name`.
* `ROOT_PASSWORD`: this is the password for a Django superuser with username `root`. Change it to something secure.

Run `docker ps` to make sure your Docker host is running. If it's not, run:

    $ docker-machine start <dockerhostname>
    $ eval "$(docker-machine env <dockerhostname>)"

Build the Docker image (you should be in the `django-docker/` directory, which contains the `Dockerfile`):

    $ docker build -t <yourname>/django-docker .

Run the Docker image you just created (the command will be explained in the `Development workflow` section below):

    $ docker run -d -p 80:80 -v $(pwd):/code --env DJANGO_PRODUCTION=false <yourname>/django-docker

Run `docker ps` to verify that the Docker container is running:

    CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS              PORTS                          NAMES
    2830610e8c87        <yourname>/django-docker   "/usr/bin/supervisord"   25 seconds ago      Up 25 seconds       0.0.0.0:80->80/tcp, 8000/tcp   focused_banach

You should now be able to access the running app through a web browser. Run `docker-machine ls` to get the local IP address for your Docker host:

    NAME           ACTIVE   DRIVER       STATE     URL                         SWARM
    mydockerhost   *        virtualbox   Running   tcp://192.168.99.100:2376

Open `http://192.168.99.100` (or your host's address, if it's different) in a browser. You should see a "Hello, world!" message.

Grab the `CONTAINER ID` from the `docker ps` output above, and use `docker kill` to stop the container:

    $ docker kill 2830610e8c87

The output of `docker ps` should now be empty:

    $ docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

