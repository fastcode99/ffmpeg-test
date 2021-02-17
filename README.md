# Prerequisite
```
apt-get install libwww-perl
```
# How to use (FFMPEG)
1. Build Image
```
docker image build -t ffmpeg -f Dockerfile.ffmpeg .
```
2. Running Container
```
docker container run --rm -it -v $(pwd)/samples:/var/tmp/samples --name ffmpeg ffmpeg <ARGUMENT>
docker container run --rm -it -v $(pwd)/samples:/var/tmp/samples --entrypoint /bin/bash --name ffmpeg ffmpeg
```
Example:

```
docker container run --rm -it -v $(pwd)/samples:/var/tmp/samples --name ffmpeg ffmpeg \
    -i /var/tmp/samples/inputs/Big_Buck_Bunny.mp4 \
    -r 1/1 \
    /var/tmp/samples/outputs/Big_Buck_Bunny.bmp
```

1 frame per second
```
docker container run --rm -it -v $(pwd)/samples:/var/tmp/samples --name ffmpeg ffmpeg \
    -i /var/tmp/samples/inputs/bun33s.mp4 \
    -vf fps=1 \
    /var/tmp/samples/outputs/bun33s_%0d.bmp
```

# How to use (youtube-dl)

1. Build Image
https://github.com/ytdl-org/youtube-dl

```
docker image build -t youtube-dl -f Dockerfile.youtube-dl .
```

2. Running container

```
docker container run --rm -it --name youtube-dl youtube-dl /bin/bash
```

3. Basic

```
$ youtube-dl --get-url <Video ID>
```