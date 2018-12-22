JENKINS_URL=$1
JENKINS_USER=$2
JENKINS_PASS=$3
JENKINS_LABELS=$4

docker build . -t ugurgungor/deployer:latest

docker run --restart=always -d -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/bin/docker ugurgungor/deployer:latest $JENKINS_URL $JENKINS_USER $JENKINS_PASS $JENKINS_LABELS