TAG = latest

build-image:
	docker build -t nameko/review-services:$(TAG) ./services

docker-tag:
	docker tag nameko/review-services:$(TAG) \
	nameko/review-services:$(TAG)

push-image:
	docker push nameko/review-services:$(TAG)
