import requests
import socket
import sys

ip = socket.gethostbyname(socket.gethostname()) 
port = 7001
url_get = F"http://{ip}:{port}/predict/get"
url_post = F"http://{ip}:{port}/predict/post"
body = {"trigger": 'start'}


if __name__ == '__main__':

    option = sys.argv[-1]

    if option == 'get':
        # Get version
        with requests.get(url_get, stream=True) as r:
            for chunk in r.iter_content(1024):  
                print(chunk)

    elif option == 'post':
        # Post Version
        with requests.post(url_post, json=body, stream=True) as r:
            for chunk in r.iter_content(1024):  
                print(chunk)
    else:
        print('Make sure to add a get or post argument to your command line')
