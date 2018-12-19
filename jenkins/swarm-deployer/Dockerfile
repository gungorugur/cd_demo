FROM ubuntu:16.04

RUN apt-get update && apt-get upgrade -y \
      && apt-get install -y sudo libltdl-dev \
      && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y net-tools && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y default-jre

RUN apt-get update && apt-get install -y wget

RUN wget -O /client.jar https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/3.14/swarm-client-3.14.jar

COPY init.sh /init.sh

RUN chmod 755 /init.sh

WORKDIR /

ENTRYPOINT [ "./init.sh" ]
