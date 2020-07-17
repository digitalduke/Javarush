# nnst simple calc


* build & run container
```shell script
$ docker build -t nnst . 
$ docker run -d -p 5000:8080 --name=nnst nnst:latest
```

* use requests from [calc.postman_collection.json](https://github.com/digitalduke/snippets/blob/nnst/nnst%20cimple%20calc.postman_collection.json)

* stop container
```shell script
$ docker stop nnst
```
