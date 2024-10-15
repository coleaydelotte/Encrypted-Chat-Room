from socket import socket, AF_INET, SOCK_STREAM

def create_server_side_connection():
    # `AF_INET`` stands for "Address Family: Internet".
    # IPv4 addresses so we are using the internet family.
    # `SOCK_STREAM` stands for "Socket Type: Stream"
    # TCP is a stream-oriented protocol, meaning that the data is transmitted in a continuous stream.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    messages = []

    # Port `8080` listening on ip: `localhost`
    server_address = ('localhost', 8080)
    server_socket.bind(server_address)
    #listening for incoming connections allowing `1` to be queued for connection.
    server_socket.listen(1)
    print("Server is listening on port 8080...")

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Connection from {client_address}")

            # Receive the data in small chunks and append it to the list
            while True:
                data = connection.recv(1024)  # Buffer size is 1024 bytes
                if data:
                    message = data.decode('utf-8')  # Decode the bytes to string
                    print(f"Received: {message}")
                    messages.append(message)  # Append to the list
                else:
                    # No more data from the client
                    print(f"Message list: {messages}")
                    break
        
        finally:
            # Clean up the connection
            connection.close()


def main():
    print(create_server_side_connection())

if __name__ == "__main__":
    main()