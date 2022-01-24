from ftplib import FTP


ip='192.168.100.3'
port=2121
ftp = FTP()
a = ftp.connect("192.168.100.3",2121)
print(a) 