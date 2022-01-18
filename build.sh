mkdir etc
if [ -z $1 ]
then
	echo "Please run the command in the format:"
	echo "./build.sh http://{rpc server here}:{ppp}"
	exit 1
fi

echo $1 >> etc/rpc
docker build -t cello .
docker volume create cello-db
docker container create --name=cello-$(whoami) cello
echo "docker container run -ti -e DISPLAY=:1 --network='host' -v /tmp/.X11-unix:/tmp/.X11-unix -v .:/app --volume cello-db:/app/db localhost/cello:latest" >> cello
chmod +x cello
./cello
