TAG = latest

build-image:
	docker build -t nameko/gateway-services:$(TAG) ./services

docker-tag:
	docker tag nameko/gateway-services:$(TAG) \
	nameko/gateway-services:$(TAG)

push-image:
	docker push nameko/gateway-services:$(TAG)
