FROM python:3.6

RUN apt-get update -qq && \
    apt-get install -y tesseract-ocr \
                libtesseract-dev

RUN pip install --upgrade pip

RUN pip3 install pyocr && \
    pip3 install pillow && \
    pip3 install boto3

ADD . /pyocr

CMD python /pyocr/myapp/main.py
