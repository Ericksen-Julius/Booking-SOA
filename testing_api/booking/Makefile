TAG = latest

build-image:
	docker build -t nameko/nameko-example-booking:$(TAG) ./booking

docker-tag:
	docker tag nameko/nameko-example-booking:$(TAG) \
	nameko/nameko-example-booking:$(TAG)

push-image:
	docker push nameko/nameko-example-booking:$(TAG)
