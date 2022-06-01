#!/bin/bash
sudo nmap -sN -iL list.txt
sudo nmap -sU -iL list.txt
sudo nmap -sC -sV -A -iL list.txt
