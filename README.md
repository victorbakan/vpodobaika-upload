# Vpodobaika2.0
## _The Simple Flask REST web server, Ever_

It can upload file with json type and print it in on web browser page



## Installation and Start (without docker)

Vpodobaika requires 
> Flask

> Python >= 3.7.3

Install the dependencies and start the server.

```sh
git clone https://github.com/victorbakan/vpodobaika.git
cd vpodobaika
pip3 install -r code/requirements.txt
python3 code/vpodobaika.py --port 3333 --address 0.0.0.0 --processes 2 --debug=true
```

## Docker
Vpodobaika is very easy to install and deploy in a Docker container.

We have regular automatic builds for this application and you can find up to date and ready to use docker image 
> [Our docker repository](https://hub.docker.com/r/bakan/vpodobaika) 

or build it by yourself - it's very easy

By default, the Docker will expose port 8030, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
git clone https://github.com/victorbakan/vpodobaika.git
cd vpodobaika
docker build -f Dockerfile ./ --tag vpodobaika:${YOUR_TAG}
```

This will create the vpodobaika image and pull in the necessary dependencies.
Be sure to swap out ${YOUR_TAG} with the actual version of vpodobaika.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port `3333` the host to
port `8030` of the Docker (or whatever port was exposed in the Dockerfile):
With docker run you can also use any additional option of the vpodobaika application, like:
> `--port 1234`

> `--processes 2`

```sh
docker run -d --restart=always --name vpodobaika -p 3333:8030/tcp vpodobaika:latest --port 8030 --processes 2
```
> Note: You can change ENTRYPOINT to CDM in Dockerfile to have more flaxability how to start/run docker container. ENTRYPOINT is by default

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://127.0.0.1:8030/
```

## Docker Compose
Please check docker section about for more details but to use this service with docker-compose localy you just need clone repo, move to folder and run

```sh
docker-compose up -d
```
This command will build dockers and run them

IMPORTANT!!!!
Docker compose goes with 2 dockers:
- nginx: used as a reverse proxy + rate limit public traffic per IP, up to 10r/s by default
- api-service: service itselfe that is behind nginx and accepts requests only from nginx 


To provide test you may use simple curl cummand in a loop.
> while true; do curl -I  http://NGINX_PUBLIC_IP:NGINX_PUBLIC_PORT/; done
