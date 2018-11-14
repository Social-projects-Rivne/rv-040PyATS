from pyats import topology

testbed	= topology.loader.load('''
devices:
    vm:
        os:	'linux'
        tacacs:
            username: pyast
        passwords:
            linux: pyastpyast
        connections:
            linux:
                protocol:	ssh
                ip:	192.168.242.44
                type: 'linux'
''')

device = testbed.devices['vm']
device.connect()
assert device.connected
output = device.execute('hostname')
print(output)
device.disconnect()
