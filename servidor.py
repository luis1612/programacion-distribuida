import socket
def principal():

    mi_socket  = socket.socket()
    mi_socket.bind(("",9090))
    mi_socket.listen(1)

    conexion, direccion = mi_socket.accept()

    while True:
        mensaje = conexion.recv(1024)
        print(direccion[0] + " dijo = "+mensaje.decode())

        conexion.send("Recibido".encode())
        if(mensaje.decode() == 'cerrar'):
            break
    print("Adios")
    conexion.close()
    mi_socket.close()

if __name__=='__main__':
    principal()