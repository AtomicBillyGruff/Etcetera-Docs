import os


if __name__ == '__main__':
    print("FFUF Scanning")
    host = 'shibboleth.htb'
    protocol = 'http'
    # reg 0 / 1 host
    scanType = 1
    if scanType == 0:
        # begin scanning
        print('regular FFUF command')
        os.system('ffuf -u {}://{}/FUZZ -w /usr/share/wordlists/dirb/common.txt'.format(protocol, host))
    else:
        print('FFUF hosts and subdomains')
        os.system('''ffuf -u {0}://{1} -H 'Host: FUZZ.{1}' -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -fw 18 '''.format(protocol, host))
