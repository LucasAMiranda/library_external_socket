from socket import *
servidor = "127.0.0.1"
porta = 43210
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)
print("Aguardando Client...")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_envida = b"Olah Cliente"
        con.send(msg_envida)
        break
    con.close()

