FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /seek_app_dir
WORKDIR /seek_app_dir
ADD requirements.txt /seek_app_dir/
RUN pip install -r requirements.txt
ADD . /seek_app_dir/