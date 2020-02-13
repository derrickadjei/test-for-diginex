FROM python:3.7-alpine
ADD uservice1.py /
WORKDIR /code   
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "uservice1.py"]