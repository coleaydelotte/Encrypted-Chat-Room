from socket import socket, AF_INET, SOCK_STREAM

class Client:
    def __init__(self):
        self.messages = []
        
    def create_client_side_connection(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 8080)
        self.client_socket.connect(self.server_address)

    def set_messages(self, messages):
        self.messages = messages

    def append_message(self, message):
        self.messages.append(message)

def main():
    print(Client.create_client_side_connection())

if __name__ == "__main__":
    main()