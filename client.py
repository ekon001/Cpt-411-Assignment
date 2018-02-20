from socket import *

serverName = '127.0.0.1'
serverPort = 11230

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = []

# Request numbers to perform operationo on the numbers
operator = input("""
                Welcome to Math Operation Server!!
                What Operation would you like perform?
                (1) Subtraction   (2) Multiplication
                (3) Addition  (4) Division (5) modulus
                >>>_
                """)

message.append(str(operator))

operand1 = str(input("enter  the first operand: >>>_ "))
operand2 = str(input("enter the second oprand: >>>_ ")) 

message.append(operand1) 
message.append(operand2)

message = " ".join(message) 


clientSocket.sendto(message, (serverName, serverPort))


result, serverAddress = clientSocket.recvfrom(4096) 
print ("the server returned " + result) 
clientSocket.close() 
