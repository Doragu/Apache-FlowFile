FROM python:3.6-slim
COPY files /kafka
WORKDIR /kafka
RUN pip3 install kafka-python
CMD ["python3", "inputjson-topic.py"]
