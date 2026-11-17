import socket 
from BWTtest import trova_bwt

HOST = "127.0.0.1"
PORT = 65432

def inizio_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server_socket.bind((HOST,PORT))
        server_socket.listen()
        print(f"Server in ascolto {HOST}:{PORT}...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"\nConnessione fatta con {addr}")
                data = conn.recv(1024)
                if not data:
                    continue

                parola = data.decode("utf-8")
                print(f"Stringa ricevuta dal cliente: '{parola}'")
                risultato = trova_bwt(parola)
                conn.sendall(risultato.encode("utf-8"))
                print(f"risultato BWT mandato al client: '{risultato}'")
if __name__ == "__main__":
    inizio_server()