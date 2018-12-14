image_id=`docker image ls | grep mongodb | grep latest | awk -F" " '{print $3}'`
docker image rm -f ${image_id}
