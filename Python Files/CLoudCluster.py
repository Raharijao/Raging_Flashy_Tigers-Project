
import io
import paramiko
from paramiko import SSHClient
#from scp import SCPClient


command = "df"

# Update the next three lines with your
# server's information

host = "login-quartzheronboxfish.cloudycluster.net"
username = "ccqadmin"
password = "hackHPC9"

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command("df")
print(stdout.read().decode())
client.close()


 
# instantiating client object and connecting it to server
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')
 
# passing SSHClient transport as the argument to SCPClient
scp = SCPClient(ssh.get_transport())
 
# Sending files to the server
scp.put('test.txt', 'test2.txt')
# Downloading files to the server
scp.get('test2.txt')
 
# Uploading the 'test' directory with its content in the
# '/home/user/dump' remote directory
scp.put('test', recursive=True, remote_path='/home/user/dump')


ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')
 
# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())
 
# generate in-memory file-like object
fl = io.BytesIO()
fl.write(b'test')
fl.seek(0)
# upload it directly from memory
scp.putfo(fl, '/tmp/test.txt')
# close connection
scp.close()
# close file handler
fl.close()


 
# instantiating client object and connecting it to server
ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')
 
# passing SSHClient transport as the argument to SCPClient
scp = SCPClient(ssh.get_transport())
 
# '/home/user/dump' remote directory
scp.put('test', recursive=True, remote_path='/home/user/dump')

#file exists

 
# make a local test file
open('deleteme.txt', 'w').write('you really should delete this]n')
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('localhost', username=getpass.getuser(),
        password=getpass.getpass('password: '))
    sftp = ssh.open_sftp()
    sftp.chdir("/tmp/")  # chnaging to directory we want to search
    try:
        print(sftp.stat('/tmp/deleteme.txt')) # checking whether file exists or not
        print('file exists')   
    except IOError:
        print('copying file')
        sftp.put('deleteme.txt', '/tmp/deleteme.txt')
    ssh.close()
except paramiko.SSHException:
    print("Connection Error")