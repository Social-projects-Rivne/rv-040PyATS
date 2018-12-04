There is a linux VM ( 192.168.242.44 , user: pyast , pass: pyastpyast ) which is available only from Softserve's network. You need
to create the following tests using given VM:
copy file from the local PC into the VM
copy file from the VM to the local PC
You have to create testbed file which will describe your device. The tests have to be executed with easypy .
Please use standard multiprotocol file transfer while implement the task.

docker sftp image: https://hub.docker.com/r/atmoz/sftp/

#docker sftp up
1. run in terminal 'docker pull atmoz/sftp' for pull image
2. run in termanal 'docker run -p 2222:22 -d atmoz/sftp foo:pass:::upload' for start 
3. try to connect with command 'sftp -P 2222 foo@127.0.0.1' using 'pass' as password 
4. if connection refused clear ssh known hosts using 'sudo mv ~/.ssh/known_hosts ~/.ssh/known_hosts_backup'
#run
5. run in terminal: 'easypy <path>/tbj.py -testbed_file <path>/docker-env.yaml'