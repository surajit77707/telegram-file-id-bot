FROM python:3.10.12-alpine 

WORKDIR /usr/src/app 

RUN chmod 777 /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

CMD [ "sh","start.sh" ]

