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
    x = bytearray(str(input('Enter the string you want to send:')), encoding='UTF-8')
    with s:
        s.connect((ip, port))
        while x != b'quit':
            s.sendall(x)
            data = s.recv(1024)
            print("Received", repr(data))
            x = bytearray(str(input('Enter the string you want to send:')), encoding='UTF-8')




if __name__ == "__main__":
    main()