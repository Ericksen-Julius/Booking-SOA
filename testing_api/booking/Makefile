TAG = latest

build-image:
	docker build -t nameko/booking-services:$(TAG) ./services

docker-tag:
	docker tag nameko/booking-services:$(TAG) \
	nameko/booking-services:$(TAG)

push-image:
	docker push nameko/booking-services:$(TAG)
