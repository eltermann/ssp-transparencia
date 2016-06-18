FROM alpine:3.1
RUN apk update
RUN apk add python-dev curl wget libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev
RUN curl https://bootstrap.pypa.io/get-pip.py | python
RUN pip install scrapy==1.1.0
WORKDIR /root
RUN wget https://github.com/eltermann/ssp-transparencia/archive/master.zip
RUN unzip master.zip
WORKDIR /root/ssp-transparencia-master/ssptransparencia
ENTRYPOINT ["/usr/bin/scrapy", "crawl", "ssptransparencia", "-a", "target_dir=/tmp/target_dir"]
