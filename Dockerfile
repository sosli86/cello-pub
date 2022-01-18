# syntax=docker/dockerfile:1
FROM ubuntu:bionic
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install python3 python3-tk python3-pip -y
RUN python3 -m pip install web3
CMD python3 /app/app.py
