from socket import *

serverPort = 11230



serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort)) 
print("The server is ready to recieve")

Subtraction = 1
Multiplication =2
Addition = 3
Division = 4
Modulus = 5

def calculator(message): 
    
   
    message = message.split(' ')
    
    operator =  int(message[0]) 
    operand1 = int(message[1])
    operand2 = int(message[2])
    
    
    
    if(operator == Subtraction):
        return operand1 - operand2
    elif(operator == Mulitiplication):
        return operand2 * operand1
    elif(operator == Addition):
        return operand1 + operand2
    elif(operator == Devision ):
        return operand1 / operand2
    elif (operator == Modulus):
        return operand2 % opereand1
    else:
        return ' error: no valid operation'

while 1: 
    message, clientAddress = serverSocket.recvfrom(4096) 
    
    resultMessage = str(calculator(message)) 
    serverSocket.sendto(resultMessage, clientAddress) 
