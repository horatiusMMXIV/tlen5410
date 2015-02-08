'''
This file defines the class Switch and its methods
'''

class Switch(object):
    def __init__(self, hostname, address):
        self.hostname = hostname
        self.address = address
        self.ports = []
        self.forwardtable = {}

    def __str__(self):
        return 'hostname: {0} address: {1}'.format(self.hostname, \
        self.address)

    def printPorts(self):
        print '\n' + self.hostname + ' port list:'
        for port, host in enumerate(self.ports):
            print 'port: {0} hostname: {1}'.format(port, host.hostname)

    def printForwardtable(self):
        print '\n' + self.hostname + ' forwardtable:'
        for address, port in self.forwardtable.iteritems():
            print 'address: {0} port: {1}'.format(address, port)

    def connect(self, device):
        self.ports.append(device)

