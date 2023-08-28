# coding:utf-8
import socket
import time

adresseip = input("Entrez une adresse IP :")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4 TCP
for port in range(1, 100):
	time.sleep(0.1)
	if sock.connect_ex((adresseip, port)):
		print ("Le port", port, "est fermé")
	else:
		print ("Le port", port, "est ouvert")
