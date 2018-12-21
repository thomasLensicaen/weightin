local_dir=$(dirname $(readlink -f $0))

VOLUME=mongodb-volume
already_exist=`docker volume ls | awk -F" " '{print$2}' | grep -e ^mongodb-volume$`
if [ -z "$already_exist" ]
then
        docker volume create ${VOLUME} 
	echo "bitch"
fi

container_id_old=`docker ps -a | grep mongodb:latest |awk -F" " '{print $1}'`
if [ ! -z "$container_id_old" ]
then
docker rm $container_id_old
fi

docker run -d --name devtest --mount source=${VOLUME},target=/app mongodb:latest
