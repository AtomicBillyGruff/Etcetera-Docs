# Creating Test Environments for Log4shell Testing


### Resource
- https://github.com/kozmer/log4j-shell-poc
- https://github.com/swisskyrepo/PayloadsAllTheThings


# pwncat 
Pwncat is a useful framework in python that is an upgrade from netcat shell allowing a more persistant and user friendly shell allowing you to live off the land and not lose your sessoins similar to how metasploit works except it does not bind to running processes like meterpreter from a framework perspective for post-exploitation.. 
> Kozmer 



### Chromium OS
- Webapp-model is why the chromebook tends to lose much of its functionality when offline. Apps don't have access by default. 
- All code that runs is virtualized and isolated within the 'sandbox'
- Comparible to an Anomoly-Based IDS where the OS is pre-prepared to work and auto-update to Google's expectations of how the device will be used. 
- Chromebook duplicates and verifies and update in a separate partition before applying the update. 
- OS Verification makes sure the filesystem and the OS and performs a signature verification of the filesystem. 

### Devloper Mode 
Enabling Developer mode on a Chromebook does not allow you to install linux in separate environment. This is done through containerization and is a feature in the base Chromebook. It does however, allow you to change the OS entirely by turning off 'OS verification'

> Developing web apps on Chrome OS is almost the same as developing web apps on any other operating system. **Any code editor, IDE , tool, or language that will run in Linux runs on Chrome OS**. - chromeos.dev

### Developer Mode Activation 
- Physically pressing the Esc , Refresh key, and Power Button will enable you to turn off os verification. 

### Enabling Crostini
- In Chrome Browser: 
		- Ctrl + F  OR system://flags
				- enable Crostini Flag
				- Requires OS verification to be turned OFF 

## Enabling Penguin Linux Environment LXC/LXD 
Settings > Advanced > Developers > Linux Development Environment 

![penguin](images/linux-container.png)

## LXC/LXD 
- LXC == Linux Containers 
- LXD == Container management system for LXC controlling networking devices, storage, and resources for the container to run on the OS. 

# Viewing Linux Containers

```
> Chromeos 

$ VMC start Termina 
$ lxc list 


```
![linux container](images/list-containers.png)
# Installing Kali in LXC 

```console
lxc launch images:kali/current/amd64 my-kali

# kali.org
```

>  Depending on you Chromebook you may need to replace amd64 with ARM64 and the linux container will install.

![kali](images/kali.png)


### Bridged Mode LXC
```
lxc config device add my-kali eth0 nic nictype=bridged parent=br0 name=eth0
```

# Vulnerabilities from ChromeOS 

| Year     | CWE      | Description|
|----------|----------|------------|
| 2019     | 190      | Overflow   | 
| 2017     | 93       | CRLF       |
| 2016     | 119      | Mem Bounds |       
| 2014     | 94       | Code Injection|        
|----------|----------|------------|----          |
             
