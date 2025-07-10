import tkinter as tk
from tkinter import scrolledtext

class ChatRoomGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Encrypted Chat Room")
        self.master.geometry("500x400")

        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=(0, 5), fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=(0, 10))

    def send_message(self, event=None):
        message = self.entry.get()
        if message.strip():
            self.display_message(f"You: {message}")
            self.entry.delete(0, tk.END)
            # Here you would typically send the message to the server
            # For demonstration, we will just echo it back
            self.display_message(f"Server: {message}")
    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatRoomGUI(root)
    root.mainloop()
