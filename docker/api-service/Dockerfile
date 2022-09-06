FROM python:3.7.3 AS base 

# Base image is up to 1GB size

ADD ./code /app 

WORKDIR /app         

#EXPOSE 8030

RUN pip3 install -r req.txt

# This is just an example of multistage build - just to be more interesting than building one stage with one image.

FROM python:3.7-alpine3.8 AS release  

# Release image is only 90MB - 10x lower so use this one for faster build, test, deployment and AWS traffic costs

WORKDIR /app
COPY --from=base /app ./
COPY --from=base /root/.cache /root/.cache


RUN pip install -r req.txt


# Choose how to run your docker container - ENTRYPOINT IS BY DEFAULT
#
#   
# !!!!! FOR DEV/STAGE/PROD ENV!!!!!!
#
# Use this to provide a docker image as executable on dev/stage/prod environments
#
# Example with CMD: you will be able to put only additional flags of the vpodobaika.py application
#
# For example: docker run -it --name vpodobaika -p 3333:8384/tcp vpodobaika:latest --port 8384 --processes 2

ENTRYPOINT ["python3.7", "vpodobaika.py"]

# 
# !!!!! FOR DEVELOPMENT ONLY!!!!!!
#
# Use this is needed to provide more flaxability for local development
#
# Example with CMD: you will be able to put anything like /bin/bash
#
# docker run -it --name vpodobaika -p 3333:3333/tcp vpodobaika:latest /bin/bash

#CMD ["python3.7", "vpodobaika.py"]
