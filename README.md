# nnst simple calc


* build & run container
```shell script
$ docker build -t nnst . 
$ docker run -d -p 5000:8080 --name=nnst nnst:latest
```

* open page at http://127.0.0.1:8080

* stop container
```shell script
$ docker stop nnst
```
