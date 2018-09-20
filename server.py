import argparse
import socket

def parse_args():
    parser = argparse.ArgumentParser(description="Starts a Python server using an IP address and a port number")
    parser.add_argument('-s', '--server', type=str, help="Server IP Address", required=True)
    parser.add_argument('-p', '--port', type=int, help="Server Port Number", required=True)
    args = parser.parse_args()
    return args.server, args.port

def main():
    # Argument parser
    ip, port = parse_args()

    # Create a socket and bind it to the port/server combination
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(1)

    conn, addr = s.accept()
    print('Server Address:', ip)
    print('Client Address:', addr)
    print("Connection Established...Closing")
    conn.close()


if __name__ == "__main__":
    main()