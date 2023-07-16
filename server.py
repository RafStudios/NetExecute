import socket

# Define the server host and port
HOST = 'localhost'  # Change this to your server IP or hostname
PORT = 12345  # Choose any available port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Server listening on', HOST, PORT)

# Accept a client connection
client_socket, client_address = server_socket.accept()
print('Client connected:', client_address)

# Read commands from a file
with open('accessclient.txt', 'r') as f:
    commands = f.readlines()

# Process and send commands to the client
for command in commands:
    command = command.strip()  # Remove leading/trailing whitespace

    # Send the command to the client
    client_socket.sendall(command.encode())
    print('Sent command:', command)

# Close the client connection
client_socket.close()
server_socket.close()
