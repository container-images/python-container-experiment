FROM fedora:25

MAINTAINER Matus Kocka, Red Hat <mkocka@redhat.com>

RUN dnf install -y bash python3 python3-numpy python3-matplotlib && dnf -y clean all

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV PATH="/usr/bin:${PATH}"

RUN mkdir /work

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"

