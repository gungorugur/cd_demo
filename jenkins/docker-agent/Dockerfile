FROM docker:18.09

RUN apk add sudo

RUN addgroup -g 1000 -S docker

RUN adduser -u 1000 -S docker -G docker

RUN echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
