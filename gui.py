import tkinter as tk
from tkinter import messagebox, simpledialog

class ChatRoomGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Encrypted Chat Room")
        
        self.chat_area = tk.Text(master, state='disabled', wrap='word')
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        self.entry = tk.Entry(master)
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)
        
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

    def send_message(self, event=None):
        message = self.entry.get()
        if message:
            # Here you would typically encrypt the message before sending
            self.display_message(f"You: {message}")
            self.entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)  # Scroll to the end