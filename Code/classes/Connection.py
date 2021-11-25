from paramiko import SSHClient
import os


class Connection:

    def __init__(self):
        self.client = SSHClient()
        self.variables = os.environ


        self.client.connect('', username='', password='')

        return self.client


    def closeConnection(self):
        self.client.close()