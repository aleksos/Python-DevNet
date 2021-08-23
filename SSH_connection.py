import paramiko
import sys

results=[]

def ssh_connection():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.0.100', username= 'admin', password= 'pwd123')

    ssh_stdin, ssh_stdout, sshstderr = client.exec.command('ss-ltn')

    for i in ssh_stdout:
        results.append(line.strip('\n'))

ssh_connection()

for i in results:
    print(i.strip())

sys.exit()