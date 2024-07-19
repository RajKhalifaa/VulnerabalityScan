import socket
import os
import sys

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode('utf-8').strip()
    except:
        return

def checkVulns(banner, filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            if line.strip("\n") in banner:
                print('[+] Server is vulnerable: ' + banner)

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] File Doesn\'t Exist!')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] Access Denied!')
            exit(0)
    else:
        print('[-] Usage: ' + str(sys.argv[0]) + " <vuln filename>")
        exit(0)

    ip = "192.168.56.5"  # Change to your Metasploitable IP address
    portlist = [21, 22, 25, 80, 110, 443, 445]
    
    for port in portlist:
        banner = retBanner(ip, port)
        if banner:
            print('[+] ' + ip + '/' + str(port) + ' ' + banner)
            checkVulns(banner, filename)

if __name__ == '__main__':
    main()
