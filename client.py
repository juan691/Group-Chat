import socket
import threading

class Client:
   def __init__(self):
       self.create_connection()

   def create_connection(self):
       self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       while 1:
           try:
               host = input('Please Enter the Host Name-->')
               port = int(input('Please Enter the port-->'))

               self.s.connect((host,port))
               break
           except:
               print('ERROR, Unable to connect to server')
       self.username = input('Please Enter Your Username-->')
       self.s.send(self.username.encode())
       message_handler = threading.Thread(target=self.handle_messages,args=())
       message_handler.start()
       input_handler = threading.Thread(target=self.input_handler,args=())
       input_handler.start()
   def handle_messages(self):
       while 1:
          print(self.s.recv(1204).decode())
   def input_handler(self):
       while 1:
          self.s.send((self.username + '-' + input()).encode())
client = Client()