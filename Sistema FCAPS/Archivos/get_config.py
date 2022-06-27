import getpass
import telnetlib
import time
import os

HOST = "192.168.56.10"
password = "cisco"
enable = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Password: ")
tn.write(password.encode('ascii')+ b'\n')

tn.read_until(b"ESW1>")

tn.write(b"enable\n")
tn.write(enable.encode('ascii')+ b'\n')
tn.write(b"terminal length 0\n")
tn.write(b"show run\n")
tn.write(b"exit\n")
out = tn.read_all()


filen = open('config.txt','w')
filen.write(out.decode('ascii'))
filen.close()
