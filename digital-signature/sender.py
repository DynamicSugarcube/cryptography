import socket
import argparse
import libcrypt
import connection as conn


def main():
	parcel = create_signature(parse_arguments())
	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((conn.HOST, conn.PORT))
	sock.send(bytes(parcel, "UTF-8"))

	data = sock.recv(conn.NBYTES)
	print(data.decode())

	sock.close()

def create_signature(message):
	max_num = int(1e+9)
	max_test = 100

	# Выбираем 2 больших простых числа
	p = libcrypt.find_primes(max_num, max_test, 1)[0]
	q = libcrypt.find_primes(2 * max_num, max_test, 1)[0]

	# Вычисляем модуль открытого ключа
	n = p * q

	# Вычисляем функцию Эйлера от n,
	# используя свойство для взаимно простых чисел
	euler_f = (p-1) * (q-1)

	# Выбираем целое число e из диапазона [1, euler_f] такое,
	# что e и euler_f должны быть взаимно простыми
	# Для простоты выбираем одно из чисел Ферма
	if euler_f < 10:
		e = libcrypt.simple_fermat_nums[0]
	elif euler_f < 100:
		e = libcrypt.simple_fermat_nums[1]
	elif euler_f < 100000:
		e = libcrypt.simple_fermat_nums[2]
	else:
		e = libcrypt.simple_fermat_nums[3]

	# Вычисляем закрытый ключ d
	d = abs(libcrypt.expanded_gcd(e, euler_f)[1]) 

	#  Шифруем сообщение message
	signature = libcrypt.expmod(message, d, n)

	return str(e) + '\n' + str(n) + '\n' + str(message) + '\n' + str(signature) + '\n'
	
def parse_arguments():
	parser=argparse.ArgumentParser()
	parser.add_argument("mess", type=int)
	arg=parser.parse_args()
	return(arg.mess)

if __name__ == "__main__":
	main()
