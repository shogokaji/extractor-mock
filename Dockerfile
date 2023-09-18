FROM public.ecr.aws/lambda/python:3.11

WORKDIR /app

COPY requirements.txt ./
RUN yum -y update \
&& yum -y install gcc libxslt-devel libxml2-devel \
&& yum clean all \
&& pip install -r requirements.txt

COPY ./ ./
