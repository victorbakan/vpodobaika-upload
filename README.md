# vpodobaika-upload
## _The Simple Flask REST web server, Ever_

It can upload file with json type and print it in on web browser page

![Build Status](https://github.com/victorbakan/vpodobaika-upload/actions/workflows/vpodobaika-upload-main.yaml/badge.svg)


## Installation and Start (without docker)

vpodobaika-upload requires 
> Flask

> Python >= 3.7.3

Install the dependencies and start the server.

```sh
git clone https://github.com/victorbakan/vpodobaika-upload.git
cd vpodobaika-upload/docker/vpodobaika-upload
pip3 install -r code/req.txt
python3 code/vpodobaika.py --port 3333 --address 0.0.0.0 --processes 2 --debug=true
```

## Docker
vpodobaika-upload is very easy to install and deploy in a Docker container.

We have regular automatic builds for this application and you can find up to date and ready to use docker image 
> [Our docker repository](https://hub.docker.com/r/bakan/vpodobaika-upload)

or build it by yourself - it's very easy

By default, the Docker will expose port 8030, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
git clone https://github.com/victorbakan/vpodobaika-upload.git
cd vpodobaika-upload/docker/vpodobaika-upload
docker build -f Dockerfile ./ --tag vpodobaika-upload:${YOUR_TAG}
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
docker run -d --restart=always --name vpodobaika-upload -p 3333:8030/tcp vpodobaika-upload:latest --port 8030 --processes 2
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
- vpodobaika-upload: service itselfe that is behind nginx and accepts requests only from nginx 


To provide test you may use simple curl cummand in a loop.
```sh
while true; do curl -I  http://NGINX_PUBLIC_IP:NGINX_PUBLIC_PORT/; done
```

## FINALTY

When the serviceis started successfully you can upload json file and check it output
> Ex with curl
```sh
curl -X POST http://127.0.0.1:8030/uploader -F file=@devops_interview_terraform_state.json  | jq .
```
