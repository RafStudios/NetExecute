import socket

# Define the server host and port
HOST = 'localhost'  # Change this to your server IP or hostname
PORT = 12345  # Use the same port number as the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print('Connected to server:', HOST, PORT)

# Receive and execute commands from the server
while True:
    # Receive data from the server
    command = client_socket.recv(1024).decode()

    # Check if the server has closed the connection
    if not command:
        break

    # Interpret and execute the command
    if command.startswith('display'):
        message = command.split('[', 1)[1].rstrip(']')
        print('Received message:', message)

# Close the client connection
client_socket.close()
