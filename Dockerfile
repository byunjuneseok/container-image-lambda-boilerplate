FROM public.ecr.aws/lambda/python:3.8

ADD lambda/ .
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["app.handler"]
