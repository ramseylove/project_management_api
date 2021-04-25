from pssh.clients import SSHClient

host = '192.168.0.57'
cmd = 'uname'
client = SSHClient(host, pkey="~/.ssh/id_rsa.pub")

host_out = client.run_command(cmd)
for line in host_out.stdout:
    print(line)