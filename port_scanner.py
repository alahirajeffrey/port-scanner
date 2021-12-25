import time
from socket import *

start_time = time.time()

if __name__ == '__main__':
    target = input("Enter host IP adress : ")
    t_IP = gethostbyname(target)
    print(f'Started scanning {t_IP}')

    for i in range(50, 60):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if(conn == 0):
            print(f'Port {i} : OPEN')
        s.close()

print(f'Time taken {time.time()- start_time}')
