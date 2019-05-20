FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt 
CMD ["python", "init/db-connect.py"]