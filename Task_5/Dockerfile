FROM python:3.6.5-slim
RUN apt-get update && apt-get install -y gcc && apt-get autoclean -y
WORKDIR /my-tests
COPY requirements.txt rabbit.py job.py ./
RUN pip install --upgrade pip wheel setuptools && \
pip install --no-cache-dir -r requirements.txt && \
rm -v requirements.txt
VOLUME /my-tests/archive
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]
ENV word=$word
CMD ["sh", "-c", "easypy job.py -word $word"]