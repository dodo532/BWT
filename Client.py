import socket

HOST = "127.0.0.1"
PORT = 65432

def inizio_client():
    word = input("inserisci la stringa da mandare al server: ")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as client_socket:
        client_socket.connect((HOST,PORT))
        client_socket.sendall(word.encode("utf-8"))

        data = client_socket.recv(1024)
        bwt_result=data.decode("utf-8")

        print(f"BWT ricevuto dal server: {bwt_result}")

if __name__ == "__main__":
    inizio_client()