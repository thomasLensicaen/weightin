local_dir=$(dirname $(readlink -f $0))

cd $local_dir/../mongo

docker build -t mongodb:latest .
