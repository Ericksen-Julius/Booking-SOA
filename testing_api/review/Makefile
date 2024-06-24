TAG = latest

build-image:
	docker build -t nameko/nameko-example-review:$(TAG) ./review

docker-tag:
	docker tag nameko/nameko-example-review:$(TAG) \
	nameko/nameko-example-review:$(TAG)

push-image:
	docker push nameko/nameko-example-review:$(TAG)
