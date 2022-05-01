#!/bin/bash

# This script is used to configure the Linux administration tools.

# check if root  
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# find writable directories and files in /etc/
echo "Checking for writable directories and files in /etc/..."
echo "-------------------------------------------------------"
find /etc/ -type d -perm -2 -ls

# find wildcards in files in /etc
echo "Checking for wildcards in files in /etc/..."
echo "-------------------------------------------------------"
find /etc/ -type f -perm /022 -ls

# list cron files
echo "Checking for cron files..."
echo "-------------------------------------------------------"
ls -l /etc/cron*
crontab -l 
systemctl status cron 

# list log files
echo "Checking for log files..."
echo "-------------------------------------------------------"
ls -l /var/log/

# check if journalctl is installed and run it
echo "Checking for journalctl..."
echo "-------------------------------------------------------"
if [ -x /usr/bin/journalctl ]; then
   echo "journalctl is installed"
   journalctl -b
   systemctl status systemd-journald.service
else
   echo "journalctl is not installed"
fi



# check if logrotate is installed and run it
echo "Checking for logrotate..."
echo "-------------------------------------------------------"
if [ -x /usr/sbin/logrotate ]; then
   echo "logrotate is installed"
   logrotate -v /etc/logrotate.conf
   systemctl status logrotate.service
else
   echo "logrotate is not installed"
fi

# check if auditd is installed and run it
echo "Checking for auditd..."
echo "-------------------------------------------------------"
if [ -x /usr/sbin/auditd ]; then
   echo "auditd is installed"
   auditctl -l
   systemctl status auditd.service
else
   echo "auditd is not installed"
fi

# list log files and check for errors
echo "Checking for errors in log files..."
echo "-------------------------------------------------------"
for i in $(find /var/log/ -type f -name "*.log"); do
   echo "Checking $i"
   echo "-------------------------------------------------------"
   grep -i error $i
done

# count of files in /var/log/
echo "Checking for files in /var/log/..."
echo "-------------------------------------------------------"
find /var/log/ -type f -ls | wc -l

# check aliases
echo "Checking for aliases..."
echo "-------------------------------------------------------"
cat /etc/profile.d/aliases.sh

# view path and environment variables
echo "Checking for path and environment variables..."
echo "-------------------------------------------------------"
echo $PATH
echo $HOME
echo $USER
echo $SHELL
echo $LANG
echo $TERM
echo $EDITOR
echo $MAIL
echo $SSH_CLIENT
echo $SSH_CONNECTION
echo $SSH_TTY
echo $SSH_AUTH_SOCK

# install tripwire and run it
echo "Checking for tripwire..."
echo "-------------------------------------------------------"
if [ -x /usr/sbin/tripwire ]; then
   echo "tripwire is installed"
   tripwire -v
   systemctl status tripwire.service
else
   echo "tripwire is not installed"
fi

# check for sudo privileges
echo "Checking for sudo privileges..."
echo "-------------------------------------------------------"
sudo -l










