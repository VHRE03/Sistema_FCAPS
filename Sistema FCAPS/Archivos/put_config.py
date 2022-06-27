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
tn.write(b"conf t\n")
tn.write(b"hostname CiscoHW\n")
tn.write(b"end\n")
tn.write(b"exit\n")
out = tn.read_all()
