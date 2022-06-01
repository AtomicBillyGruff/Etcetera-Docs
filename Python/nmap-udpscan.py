import os
import re
import subprocess
if __name__ == '__main__':
    print('-')
    ip = '10.10.11.124'
    # ports =subprocess.run('''ports=sudo nmap --min-rate=5000 -sU {}'''.format(ip))
    ports = subprocess.run(['sudo', 'nmap', '--min-rate=5000', '-sU', ip], capture_output=True)
    ports = ports.stdout.splitlines()
    # print(ports)
    opnPorts = []
    for item in ports:
        item = str(item)
        if re.search(' open ', str(item)):
            opnPorts.append(item.lstrip("b'").rsplit('  ')[0].rsplit('/udp')[0])
    for port in opnPorts:
        subprocess.run(['sudo', 'nmap', '-sC', '-sV', '-sU', '-p {}'.format(port), ip ])


    # os.system('sudo nmap -sC -sV -p- -sU')
