from ftplib import FTP

server_address = 'test.rebex.net'
username = 'demo'
password = 'password'

ftp = FTP(server_address)

ftp.login(username, password)

directory_contents = ftp.nlst()

print("Directory Contents:")
for item in directory_contents:
    print(item)

ftp.quit()


