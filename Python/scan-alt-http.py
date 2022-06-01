import os


if __name__ == '__main__':
    FFUF = False
    # ip = input('ip address')
    # port = str(input('''port or port/s ',' deliom'''))
    ip = '10.10.11.133'
    port = '8443, 10250'
    ports = [8443, 10250]
    # if ',' in port:
    #     for item in port.split(','):
    #         ports.append(item.strip(' '))

    print('Getting Ports')

    for port in ports:
        print(" curling port {} on ip {}: ".format(port, ip))
        os.system('curl https://{}:{}/ -k'.format(ip, port))
        if len(os.system('curl https://{}:{}/pods -k'.format(ip, port)) > 100):
            print("install kube")
        if FFUF:
            os.system('ffuf -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt -u https://{}:{}/FUZZ'.format(ip, port))
            os.system('ffuf -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt -u http://{}:{}/FUZZ'.format(ip, port))








