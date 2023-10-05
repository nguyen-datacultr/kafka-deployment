echo "Creating pv and storage..."
kubectl apply -f /Users/ryan/playground/devops/kafka/storage/pv-kafka.yaml
kubectl apply -f /Users/ryan/playground/devops/kafka/storage/pv-zoo.yaml
kubectl apply -f /Users/ryan/playground/devops/kafka/storage/sc-kafka.yaml
kubectl apply -f /Users/ryan/playground/devops/kafka/storage/sc-zoo.yaml