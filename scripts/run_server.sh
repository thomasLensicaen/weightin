VENV=".venv_weightin"
local_dir=$(dirname $(readlink -f $0))
cd $local_dir/../weightin
echo $(pwd)
nohup ../${VENV}/bin/python main.py ../configs/config.json > server_logs 2>&1 &
