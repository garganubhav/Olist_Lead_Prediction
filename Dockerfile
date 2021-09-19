FROM ubuntu:18.04

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update
RUN apt-get -y install git
RUN apt-get install -y --no-install-recommends \
    python3.5 \
    python3-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "python3", "./app.py" ]
