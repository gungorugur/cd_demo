echo Downloading sonarqube docker image

docker pull sonarqube:lts

echo Deploying sonarqube service

docker stack deploy -c docker-compose-stack.yml sonarqube