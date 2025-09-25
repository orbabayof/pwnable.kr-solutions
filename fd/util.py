from pwn import ssh

def connectPwnable(challenge : str):
    return ssh(host="pwnable.kr", port=2222 ,user=challenge, password="guest") 

def runExec(connection, name: str, *argv):
    name = './' + name 
    for arg in argv:
        name += ' ' + str(arg)
    return connection.system(name)

class Executable:
    def __init__(self, name : str, connection : ssh):
        self.name = name
        self.connection = connection

    def run(self, *argv):
        command = './' + self.name
        for arg in argv:
           command += ' ' + str(arg) 
        return self.connection.system(command)


    

