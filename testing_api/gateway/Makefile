TAG = latest

build-image:
	docker build -t nameko/nameko-example-gateway:$(TAG) ./gateway

docker-tag:
	docker tag nameko/nameko-example-gateway:$(TAG) \
	nameko/nameko-example-gateway:$(TAG)

push-image:
	docker push nameko/nameko-example-gateway:$(TAG)
