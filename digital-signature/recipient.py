import libcrypt

f = open("message.txt", "r")
s=f.read()
a=s.split('\n')
e=int(a[0])
n=int(a[1])
m=int(a[2])
s=int(a[3])
decr_m=libcrypt.expmod(s,e,n)
if decr_m==m:
    print('ok')
else:
    print('not ok')
f.close()
