#!/usr/bin/env python

import time
from netmiko import redispatch
from netmiko.ssh_dispatcher import ConnectHandler

jumpserver = {
    'device_type': 'terminal_server',
    'ip': '10.108.16.104',
    'username': 'd856095',
    'password': 'Pass@1234',
#	'global_delay_factor':2
}

print("Connecting %s" % jumpserver)

net_connect = ConnectHandler(**jumpserver)
print(net_connect.find_prompt())

filewrite = open("output1.txt", "a")

file_obj = open("officeDevice.txt", "r")
for line in file_obj:
    print("Connecting ***** %s" % line)
    net_connect.write_channel("mtrad " + line)
    time.sleep(1)
    net_connect.read_channel()

    redispatch(net_connect, device_type='cisco_ios_telnet')
    output = net_connect.send_command("show version | i IOS")
    output = net_connect.send_command("show mod | i 10GE")
    print(output)
    net_connect.send_command("exit", expect_string="mobboss2")
    filewrite.write("\n \n" + line + "\n")
    filewrite.write("-------------------------- \n")
    filewrite.write(output)

net_connect.disconnect()
filewrite.close()