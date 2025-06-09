import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sender ke ander receiver ka ip
# receiver ke ander sender ka ip
ip_add = '192.168.72.36'
port_num = 7000   # 0--65536
complete_add = (ip_add,port_num)
s.bind(complete_add)
while True:
    message = s.recv(1024)
    print(message)
    data = message[0]
    data = '\n' # escape char
    print(data.encode('ascii'))