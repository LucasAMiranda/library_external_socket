from socket import *

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida = ""

while saida != "X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (servidor, porta))
    dados, origem = obj_socket.recvfrom(65535) #range máximo da porta
    print("Resposta do servidor ", dados.decode())
    saida = input("Digite <X> para sair: ").upper()

#fechando conexão para liberar a porta
obj_socket.close()