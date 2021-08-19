FROM python:3.9
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update && \
	apt-get -y install aria2

WORKDIR /root/
ADD infosec.py ./

RUN pip install requests

ENTRYPOINT ["python", "infosec.py"]