# 🔐 Encrypted Chat Room

A terminal-based encrypted chat room built using Python sockets. This project allows multiple users to connect to a server and exchange messages securely. Messages are encrypted in transit using symmetric encryption (AES via the `cryptography` library with Fernet).

## 📌 Features

- ✅ Server-client architecture using Python `socket` (`AF_INET`, `SOCK_STREAM`)
- ✅ Supports multiple users concurrently using `threading`
- ✅ Real-time message broadcasting
- ✅ End-to-end encryption using **Fernet** (AES-based)
- ✅ Terminal interface for simplicity and portability
- 🛠️ (Optional) Docker support in the future

---

## ⚙️ How It Works

The system consists of two Python files:

- **`server.py`** – Accepts incoming connections, receives messages, and broadcasts them to all connected users.
- **`client.py`** – Connects to the server, encrypts messages before sending, and decrypts incoming messages in real-time.

---

## 🧪 Development Milestones

1. ✅ Create a basic TCP connection between server and client.
2. ✅ Implement `ping` and `pong` test messages for handshake.
3. ✅ Support for **multiple users** concurrently.
4. ✅ Implement real-time **message sending and receiving**.
5. ✅ Encrypt messages during transfer using **Fernet (AES)**.
6. 🚧 Optional: Dockerize the app using `Docker` and `docker-compose`.

---

## 🔐 Encryption Details

Messages are encrypted using **Fernet symmetric encryption**, which:

- Uses AES in CBC mode with PKCS7 padding
- Ensures confidentiality and integrity of messages
- Requires only a **shared key** (generated once per session or stored securely)

> Requires the `cryptography` library:
```bash
pip install cryptography
```

## Authors
<ol>
    <li> Cole Aydelotte
    <li> Omer Qureshi
</ol>