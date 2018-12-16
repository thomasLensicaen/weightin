local_dir=$(dirname $(readlink -f $0))
tmp_dir=$1
cp -r ../configs .
cp -r ../scripts .
cp ../Makefile .
cp -r ../weightin .
cp -r ../static .
cp -r ../tests .
