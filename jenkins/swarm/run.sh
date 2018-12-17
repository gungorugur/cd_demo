JENKINS_URL=$1
JENKINS_USER=$2
JENKINS_PASS=$3
JENKINS_LABELS=$3

docker build . -t ugurgungor/provisioning:latest

docker run -d -v /var/run/docker.sock:/var/run/docker.sock -v /usr/bin/docker:/bin/docker ugurgungor/provisioning:latest $JENKINS_URL $JENKINS_USER $JENKINS_PASS $JENKINS_LABELS