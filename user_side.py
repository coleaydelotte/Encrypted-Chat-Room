from socket import socket, AF_INET, SOCK_STREAM

def create_client_side_connection():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8080)
    client_socket.connect(server_address)

def main():
    print(create_client_side_connection())

if __name__ == "__main__":
    main()