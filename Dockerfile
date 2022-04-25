FROM python:3.9-slim
WORKDIR /opt/app

#RUN apt-get update -y 
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY src/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY src/. .
EXPOSE 5000
CMD gunicorn -w 1 -b 0.0.0.0:5000 wsgi:server
