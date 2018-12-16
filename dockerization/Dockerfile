FROM alpine:3.8

RUN apk add --no-cache python3 && \
python3 -m ensurepip && \
rm -r /usr/lib/python*/ensurepip && \
pip3 install --upgrade pip setuptools && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

# IS destination what you expect
COPY -r configs .
COPY -r scripts .
COPY Makefile .
COPY -r weightin .
COPY -r static .
COPY -r tests .

RUN sh scripts/create_venv.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

#as a script
CMD VENV/bin/python main_server.py
