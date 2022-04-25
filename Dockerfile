FROM python:3.7
WORKDIR /opt/app
COPY src/requirements.txt .
#RUN apt-get update -y 
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 
COPY src/. .
EXPOSE 5000
#CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
CMD gunicorn -w 1 -b 0.0.0.0:5000 wsgi:server
