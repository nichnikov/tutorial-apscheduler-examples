FROM python:3.10-slim
# FROM python:3.8-slim
# FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . /app

# RUN apt-get update && apt-get install -y build-essential libpoppler-cpp-dev pkg-config python-dev

# install dependencies
# RUN pip install --proxy=http://proxy.dev.aservices.tech:8080 --upgrade pip
# RUN pip install --proxy=http://proxy.dev.aservices.tech:8080 -r requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# run the command
CMD ["python", "./fa_scheduler_BackgroundScheduler.py"]
