from centos:7
RUN mkdir -p /app/api
RUN yum install epel-release -y
RUN yum install python-pip -y
RUN pip install flask
add https://github.com/raghualapati/httpserver/raw/master/api.py /app/api
RUN chmod 700 /app/api/api.py
ENTRYPOINT ["python" "/app/api/api.py"]
EXPOSE 8080
