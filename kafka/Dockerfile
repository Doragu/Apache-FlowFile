FROM python:3.6
ADD . /code
WORKDIR /code
COPY input_json/*.json /code/input_json/
RUN pip install -r requirements.txt 
CMD ["python", "inputjson-topic.py"]