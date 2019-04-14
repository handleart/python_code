# -*- coding: utf-8 -*-

def strxor(s1,s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))


s1 = '09e1c5f70a65ac519458e7e53f36'
s2 = 'attack at dawn'

#print "6c73d5240a948c86981bc294814d".decode('hex')

#print strxor(strxor("6c73d5240a948c86981bc294814d".decode('hex'), "attack at dawn"), "attack at dusk").encode('hex')

a = "attack at dawn"
b = "09e1c5f70a65ac519458e7e53f36"
f = "attack at dusk"

print strxor(strxor(b.decode('hex'), a), f).encode('hex')


for i in xrange(len(b) / 2):
	#print 2*i, 2* +2 , b[2*i: 2*i + 2]
	print(b[2*i: 2*i + 2])



