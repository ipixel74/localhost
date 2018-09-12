#!/usr/bin/env python

import http.server
import socketserver
import webbrowser
import urllib.parse
from socket import * 
import os

if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print ('\n')
print ('\n')
print ('\n')
print ('\n')




print (         " ========================================================================= ")

print (         " ========================================================================= ")

print (         " ========================= PIXEL Server 4774 ============================= ")

print (         " ========================================================================= ")

print (         " =================== Use the Python localhost Server ===================== ")

print (         " ========================================================================= ")
print ('\n')
print ('\n')
print ('\n')
print ('\n')

print (                             "[ .. Open your localhost web site in a browser .. ] \n")

listpo = ['port']
port = int(input('Enter Port : '))
url = "http://127.0.0.1:" + str(port)
h = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",port),h)
print (("Server is up --> 127.0.0.1:"),port)
webbrowser.open(url)
httpd.serve_forever()


