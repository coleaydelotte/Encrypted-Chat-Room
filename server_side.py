import socket
import threading

class Server:
    def __init__(self):
        self.clients = []  # List to hold all connected client sockets
        self.lock = threading.Lock()  # For thread-safe access to clients list

    def broadcast(self, message, sender_socket):
        """Send a message to all clients except the sender."""
        with self.lock:
            for client in self.clients:
                if client != sender_socket:
                    try:
                        client.sendall(message.encode('utf-8'))
                    except:
                        client.close()
                        self.clients.remove(client)

    def handle_client(self, connection, client_address):
        print(f"Connection from {client_address}")
        with self.lock:
            self.clients.append(connection)

        try:
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                message = data.decode('utf-8')
                print(f"Received from {client_address}: {message}")
                self.broadcast(f"{client_address[0]}: {message}", connection)
        finally:
            with self.lock:
                if connection in self.clients:
                    self.clients.remove(connection)
            connection.close()
            print(f"Client {client_address} disconnected.")

    def create_server_side_connection(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 8080))
        server_socket.listen()
        print("Server is listening on port 8080...")

        while True:
            print("Waiting for a connection...")
            connection, client_address = server_socket.accept()
            client_thread = threading.Thread(
                target=self.handle_client, args=(connection, client_address)
            )
            client_thread.start()

def main():
    server = Server()
    server.create_server_side_connection()

if __name__ == "__main__":
    main()
