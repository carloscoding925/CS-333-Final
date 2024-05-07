FROM python:3.10

WORKDIR /Final Project

COPY . .

CMD [ "python", "driver.py" ]
