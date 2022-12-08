Code:
!docker run --platform linux/amd64 -it --rm \
  -p 8500:8500 \
  -v $(pwd)/clothing-model:/models/clothing-model/1 \
  -e MODEL_NAME="clothing-model" \
  tensorflow/serving:2.7.0

Error:
Status: Downloaded newer image for tensorflow/serving:2.7.0
[libprotobuf FATAL external/com_google_protobuf/src/google/protobuf/generated_message_reflection.cc:2345] CHECK failed: file != nullptr: 
terminate called after throwing an instance of 'google::protobuf::FatalException'
  what():  CHECK failed: file != nullptr: 
qemu: uncaught target signal 6 (Aborted) - core dumped
/usr/bin/tf_serving_entrypoint.sh: line 3:     8 Aborted                 tensorflow_model_server --port=8500 --rest_api_port=8501 --model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} "$@"


docker pull emacski/tensorflow-serving:latest


docker run -it --rm \
  -p 8500:8500 \
  -v $(pwd)/clothing-model:/models/clothing-model/1 \
  -e MODEL_NAME="clothing-model" \
  emacski/tensorflow-serving:latest-linux_arm64


pip install grpcio==1.42.0 
pip3 install --no-deps tensorflow-serving-api



### python gateway.py
Traceback (most recent call last):
  File "/Users/daniel/ml-zoomcamp/10-kubernetes/gateway.py", line 5, in <module>
    import grpc
  File "/Users/daniel/miniconda3/envs/tensorflow/lib/python3.9/site-packages/grpc/__init__.py", line 22, in <module>
    from grpc import _compression
  File "/Users/daniel/miniconda3/envs/tensorflow/lib/python3.9/site-packages/grpc/_compression.py", line 15, in <module>
    from grpc._cython import cygrpc
ImportError: dlopen(/Users/daniel/miniconda3/envs/tensorflow/lib/python3.9/site-packages/grpc/_cython/cygrpc.cpython-39-darwin.so, 0x0002): symbol not found in flat namespace '_CFRelease'

Solution
pip uninstall grpcio
export GRPC_PYTHON_LDFLAGS=" -framework CoreFoundation"
pip install grpcio --no-binary :all:
conda install protobuf

grpcio==1.51.1


pipenv install grpcio==1.51.1 flask keras-image-helper gunicorn

pipenv install tensorflow-protobuf==2.7.0


pipenv shell 
python gateway.py 

Traceback (most recent call last):
  File "/Users/daniel/ml-zoomcamp/10-kubernetes/gateway.py", line 5, in <module>
    import grpc
  File "/Users/daniel/.local/share/virtualenvs/10-kubernetes-Ml12-i0S/lib/python3.9/site-packages/grpc/__init__.py", line 22, in <module>
    from grpc import _compression
  File "/Users/daniel/.local/share/virtualenvs/10-kubernetes-Ml12-i0S/lib/python3.9/site-packages/grpc/_compression.py", line 20, in <module>
    from grpc._cython import cygrpc
ImportError: dlopen(/Users/daniel/.local/share/virtualenvs/10-kubernetes-Ml12-i0S/lib/python3.9/site-packages/grpc/_cython/cygrpc.cpython-39-darwin.so, 0x0002): symbol not found in flat namespace '_CFRelease'

pipenv install grpcio --no-binary :all:

pipenv install grpcio==3.19.0

pipenv run python gateway.py




#### Example: Create a docker image
docker build -t zoomcamp-10-model:xception-v4-001 \
  -f image-model.dockerfile .

### Run the image
docker run -it --rm \
  -p 8500:8500 \
  zoomcamp-10-model:xception-v4-001


### Question
docker build -t zoomcamp-10-gateway:002 \
  -f image-gateway.dockerfile .

docker run -it --rm \
  -p 9696:9696 \
  zoomcamp-10-gateway:001


docker-compose up -d


curl localhost:9696/ping


Kubernetes



kubectl config delete-cluster kind-kind

kind delete cluster

kind get clusters 

###### 
kind create cluster

kubectl get service
kubectl get pod
kubectl get deployment

kubectl apply -f deployment.yaml

kind load docker-image ping:v001
kubectl port-forward ping-deployment-7df687f8cd-tfkgd 9696:9696

kubectl apply -f service.yaml
kubectl port-forward service/ping 8080:80

kind load docker-image zoomcamp-10-model:xception-v4-001

kubectl apply -f model-deployment.yaml

kubectl describe pod

kubectl port-forward tf-serving-clothing-model-85cd4b7fc9-rntfw 8500:8500

kubectl apply -f model-service.yaml

kubectl port-forward service/tf-serving-clothing-model 8500:8500

kind load docker-image zoomcamp-10-gateway:002

kubectl get pod

kubectl exec -it ping-deployment-577d56ccf5-p2bdq -- bash

curl localhost:9696/ping

curl ping.default.svc.cluster.local/ping

curl tf-serving-clothing-model.default.svc.cluster.local/8500

kubectl apply -f gateway-deployment.yaml

kubectl port-forward gateway-597bd6bbf-l6hf5 9696:9696

kubectl apply -f gateway-service.yaml

kubectl port-forward service/gateway 8080:80






kubectl delete -f deployment.yaml


kubectl run myapp --image=zoomcamp-model:v001


kubectl port-forward service/credit-card 9696:80