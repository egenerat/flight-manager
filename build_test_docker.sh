old_container_id=$(docker ps -a |grep webserver_test_pages | cut -d " " -f 1)
echo $old_container_id
if [ -n "$old_container_id" ]; then
	echo "cleanup all container"
	docker rm -f $old_container_id
fi

cd tests_util/
docker build -t fm/webserver_test_pages .
docker run -d --name webserver_test_pages -p 9080:80 fm/webserver_test_pages
cd ..