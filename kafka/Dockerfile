FROM python:3.6
ADD . /code
WORKDIR /code
COPY input_json/*.json /code/input_json/
RUN pip3 install -r requirements.txt 
CMD ["python3", "inputjson-topic.py"]