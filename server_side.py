from socket import socket, AF_INET, SOCK_STREAM

def create_server_side_connection():
    # `AF_INET`` stands for "Address Family: Internet".
    # IPv4 addresses so we are using the internet family.
    # `SOCK_STREAM` stands for "Socket Type: Stream"
    # TCP is a stream-oriented protocol, meaning that the data is transmitted in a continuous stream.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Port `8080` listening on ip: `localhost`
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)
    #listening for incoming connections allowing `1` to be queued for connection.
    server_socket.listen(1)
    print("Server is listening on port 8080...")

    return None

def main():
    print(ping())

if __name__ == "__main__":
    main()