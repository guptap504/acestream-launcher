# acestream-launcher
Acestream launcher using the ikatson/aceproxy docker image

## Usage
acestream [Acestream URL]

It uses mpv by default. To change it, change it in the script.

## Requirements
- Python 3
- Docker
- Media player capable of playing network streams

## Installing docker image
Run 'sudo docker run -t -p 8000:8000 ikatson/aceproxy' on your terminal.

## Installing launcher
Simply run 'sudo bash ./install.sh' on your terminal.
