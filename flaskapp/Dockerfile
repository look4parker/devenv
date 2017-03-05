FROM python

RUN pip install Flask
RUN pip install elasticsearch
RUN pip install requests

RUN mkdir -p /var/www/app

ENV FLASK_APP web.py

WORKDIR /var/www/app

EXPOSE 5000

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
