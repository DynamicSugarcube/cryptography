import socket

import libcrypt
import connection as conn

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((conn.HOST, conn.PORT))
	sock.listen(conn.NCLIENTS)

	while True:
		client_connection, client_address = sock.accept()
		print("Connected client: " + str(client_address))
		client_data = client_connection.recv(conn.NBYTES)
		print("Received data:\n" + client_data.decode())
		ack = check_signature(client_data.decode())
		client_connection.send(bytes(ack,"UTF-8"))
		client_connection.close()
		
	sock.close()

def check_signature(data):
	arr = data.split('\n')
	e = int(arr[0])
	n = int(arr[1])
	m = int(arr[2])
	s = int(arr[3])
	decr_m=libcrypt.expmod(s,e,n)
	if decr_m == m:
		return "ok"
	else:
		return "not ok"

if __name__ == "__main__":
	main()
