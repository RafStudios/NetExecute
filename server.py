#copyright rafstudios
#Server For NetExecute
import socket

HOST = 'localhost'
PORT = 8080

def handle_command(command):
    if command.startswith("display"):
        text = command.split("[")[1].split("]")[0]
        return f"Displaying: {text}"
    else:
        return "Invalid command"

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode()
                response = handle_command(command)
                conn.sendall(response.encode())

start_server()
