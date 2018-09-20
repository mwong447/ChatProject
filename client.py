import argparse
import socket

# Recycled argument fetcher from the server
def parse_args():
    parser = argparse.ArgumentParser(description="Starts a Python server using an IP address and a port number")
    parser.add_argument('-s', '--server', type=str, help="Server IP Address", required=True)
    parser.add_argument('-p', '--port', type=int, help="Server Port Number", required=True)
    args = parser.parse_args()
    return args.server, args.port

def main():
    ip, port = parse_args()
    print("Attempting to connect to server at: ", ip, "Port:", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    print("Connection to Server Established")
    s.close()
