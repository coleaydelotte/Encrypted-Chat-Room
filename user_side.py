import socket
import threading

class Client:
    def __init__(self):
        self.messages = []
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def create_client_side_connection(self):
        self.client_socket.connect(('localhost', 8080))
        print("Connected to server.")
        
        # Start a background thread to receive messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        # Main loop to send messages
        while True:
            message = input()
            if message.lower() == 'exit':
                print("Disconnecting...")
                self.client_socket.close()
                break
            self.client_socket.sendall(message.encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    decoded = data.decode('utf-8')
                    self.messages.append(decoded)
                    print(f"\n{decoded}\n> ", end="")
                else:
                    break
            except:
                break

def main():
    client = Client()
    client.create_client_side_connection()

if __name__ == "__main__":
    main()
