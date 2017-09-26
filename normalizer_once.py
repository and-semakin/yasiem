from datetime import datetime

def normalize(line):
    #  undo priority
    # <123>  <88>-
    prio = line[1:5]
    if not prio.isdigit():
        prio = prio[:-1]
    prio = int(prio)
    prio = {'facility': prio // 8, 'severity': prio % 8}
    
    line = line[5:]
    
    if(line.startswith('%Antivirus%')):
        
        line = line[len('%Antivirus% '):]
        splitted = line.split(";", maxsplit=3)
        dt = datetime.strptime(splitted[0], '%Y-%m-%d-%H-%M-%S-%f')
        arm = splitted[1]
        document = splitted[2]
        action = splitted[3].rstrip("\x00\n")
        return {'priority': prio, 'source': 'avr', 'dt': dt, 'arm': arm, 'doc': document, 'act': action}
        
    elif(line.startswith('%OS-Login%')):
        line = line[len('%OS-Login% '):]
        splitted = line.split(";", maxsplit=2)
        dt = datetime.strptime(splitted[0], '%Y-%m-%d-%H-%M-%S-%f')
        worker = splitted[1]
        action = splitted[2].rstrip("\x00\n")
        return {'priority': prio, 'source': 'osl', 'dt': dt, 'worker': worker, 'act': action}
        
    elif(line.startswith('%AccessControl%')):
        line = line[len('%AccessControl% '):]
        splitted = line.split(";")
        #print("AZAZLO")
        #print(splitted)
        #print("AZAZLO")
        dt = datetime.strptime(splitted[0], '%Y-%m-%d-%H-%M-%S-%f')
        ipv4 = splitted[1]
        arm = splitted[2]
        os = splitted[3]
        user = splitted[4]
        action = splitted[5].rstrip("\x00\n")
        return {'priority': prio, 'source': 'acs', 'dt': dt, 'ipv4': ipv4, 'arm': arm, 'user': user, 'os': os, 'act': action}
    else:
        return {'act': 'Parse error.'}

if __name__ == "__main__":
    for line in open('example.log'):
        print(normalize(line))