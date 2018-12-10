import requests
import sys
import json
import time

NEXUS_URL = sys.argv[1]
NEXUS_USER = sys.argv[2]
NEXUS_PASS = sys.argv[3]

auth = (NEXUS_USER, NEXUS_PASS)

# default wait time for nexus startup
time.sleep(60)

iteration = 0
isHealthy = False

while iteration < 10:
    try:
        r = requests.get(NEXUS_URL + "/service/metrics/healthcheck", auth=auth)
        isHealthy = r.status_code == 200
        if isHealthy:
            break
        else:
            print("Current status code:{} Wait 10 secs for next health check..".format(r.status_code))
    except requests.exceptions.ConnectionError as connectionError:
        print(connectionError)
    finally:
        time.sleep(10)
        iteration = iteration+1

if isHealthy:
    print("Nexus is in healthy state.")
else:
    print("Nexus is not in healthy state!!!")
    sys.exit(-1)

createRepositoryScript = {
    "name": "create-docker-registry",
    "type": "groovy",
    "content": "repository.createDockerHosted('docker-private', 8082, null, 'default' ,true, true, org.sonatype.nexus.repository.storage.WritePolicy.ALLOW_ONCE, true)"
}

r = requests.post(NEXUS_URL + '/service/rest/v1/script/',
                  json=createRepositoryScript,
                  auth=auth
                  )

if r.status_code != 204:
    print("Repository script creation problem!!, Status code:{}".format(r.status_code))
    sys.exit(-1)

r = requests.post(NEXUS_URL + '/service/rest/v1/script/create-docker-registry/run',
                  data='create-docker-registry',
                  auth=auth,
                  headers={'content-type': 'text/plain'}
                  )

if r.status_code != 200:
    print("Repository script execution problem!!, Status code:{}".format(r.status_code))
    sys.exit(-1)

r = requests.delete(NEXUS_URL + '/service/rest/v1/script/create-docker-registry',
                    auth=auth,
                    )

if r.status_code != 204:
    print("Repository script deleting problem!!, Status code:{}".format(r.status_code))
    sys.exit(-1)

print("Docker registry created.")