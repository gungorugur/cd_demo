docker build . -t ugurgungor/jenkins:lts

docker stack deploy -c docker-compose-stack.yml jenkins
