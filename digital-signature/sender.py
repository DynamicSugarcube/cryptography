import libcrypt

max_num = int(1e+9)
max_test = 100

message = 1488

# Выбираем 2 больших простых числа
p, q = libcrypt.find_primes(max_num, max_test, 2)

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

f = open("message.txt", "w")
f.write(str(e) + '\n' +
		str(n) + '\n' +
		str(message) + '\n' +
		str(signature))
f.close()
