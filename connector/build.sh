export DOCKER_ORG=unibna
export CONNECTOR_NAME="postgres-demo"
docker build . --platform=linux/amd64 -t ${DOCKER_ORG}/${CONNECTOR_NAME}-connect-debezium:$1
docker push ${DOCKER_ORG}/${CONNECTOR_NAME}-connect-debezium:$1