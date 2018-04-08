import sys
import os
import psutil

def dockerRunning():
    for pid in psutil.pids():
        if (psutil.Process(pid)).name() == "dockerd":
            return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage:", "myscript...[acestream URl]", sep='\n')
        exit()
    if dockerRunning() is not True:
        print("Please run 'sudo docker run -t -p 8000:8000 ikatson/aceproxy' and try again")
        exit()
    
    acestream_id = (sys.argv[1].split('/'))[-1]
    docker_url = "http://localhost:8000/pid/" + acestream_id + "/stream.mp4"
    print("Starting stream..")
    os.system("mpv " + docker_url)

if __name__ == "__main__":
    main()
    