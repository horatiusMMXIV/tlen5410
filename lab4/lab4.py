'''
Sources:
1. http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/
- How to send an email with python and smtp.

'''

import re
import smtplib
import lab1

def emailAdmin(error):
    fromaddr = "bobdallas.tlen5540@gmail.com"
    password = "netman2015"
    toaddrs = "robert.werthman@colorado.edu"
    msg = 'To:' + toaddrs + '\n' + 'From: ' + fromaddr + '\n' + 'Subject:lab4 \n'
    msg = msg + '\n' + error + '\n\n'
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def handleConfigTrap(ip):
    ip = ip.strip('[]')
    lab1.getConfig(ip)
    lab1.saveConfig(ip)
    emailAdmin("Router {0}'s config changed!".format(ip))

def handleTrap(trap):
    prog = re.compile('(\[[0-9]+\.[0-9]+\.[0-9]+\.[0-9]\])')
    ip = ''
    for line in trap:
        matchIP = prog.search(line)
        if matchIP:
            ip =  matchIP.group(0)
        if "SNMPv2-SMI::enterprises.9.9.43." in line:
            handleConfigTrap(ip)
            break

def main():
    trap = []
    while True:
        try:
            line = raw_input()
            trap.append(line)
        except EOFError:
            break
    handleTrap(trap)

if __name__=='__main__':
    main()
