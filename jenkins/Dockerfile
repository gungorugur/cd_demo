FROM jenkins/jenkins:lts

USER root
RUN apt-get update \
      && apt-get upgrade -y \
      && apt-get install -y sudo libltdl-dev \
      && rm -rf /var/lib/apt/lists/*
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers

COPY init.sh /init.sh
RUN chmod 777 /init.sh

USER jenkins

ENTRYPOINT ["sh", "-c", "/init.sh","jenkins"]                    

