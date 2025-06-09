import socket

try:
    # creating a socket // connecting to server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # dgram = datagram -- network ke trhough data transfer
    print('Socket successfully created')
    
    ip_add = '192.168.72.36'
    port_num = 7000   # 0--65536
    target_add = (ip_add,port_num)
    message = input("Enter your message")
    encripted_message = message.encode('ascii')
    s.sendto(encripted_message,target_add)
    
except Exception as msg:
    print(msg)