import os


ip_server = os.environ.get("IP_SERVER")
ip_port = os.environ.get("PORT_SERVER")

ip_port = 10001 if ip_port is None else ip_port
ip_server = "127.0.0.1" if ip_server is None else ip_server


def start_push():
    while True:
        pass


if __name__ == '__main__':
    start_push()
