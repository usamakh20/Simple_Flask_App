FROM python:3.6-alpine
LABEL maintainer="USAMA KHALID <i191236@nu.edu.pk>"
WORKDIR /project2
ADD . /project2
RUN pip install -r requirements.txt
CMD ["flask","run","--host=0.0.0.0"]
