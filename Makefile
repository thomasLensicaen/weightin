env:
	sh scripts/create_venv.sh
run:
	sh scripts/run_server.sh

test:
	sh scripts/run_test.sh

build_mongo_docker:
	sh scripts/build_mongo_docker.sh

run_mongo_docker:
	sh scripts/launch_mongo_docker.sh

clean_docker_images:
	sh scripts/clean_docker_images.sh
