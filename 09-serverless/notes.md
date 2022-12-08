docker build --platform linux/amd64 -t clothing-model .

docker run -it --rm -p 8080:8080 --platform linux/amd64 clothing-model:latest


homework

docker build --platform linux/amd64 -t dino_dragon-model .

docker run -it --rm -p 8080:8080 --platform linux/amd64 dino_dragon-model:latest