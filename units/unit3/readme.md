docker sftp image: https://hub.docker.com/r/atmoz/sftp/

1. run in terminal 'docker pull atmoz/sftp' for pull image
2. run in termanal 'docker run -p 2222:22 -d atmoz/sftp foo:pass:::upload' for start 
3. try to connect with command 'sftp -P 2222 foo@127.0.0.1' using 'pass' as password 
4. if connection refused clear ssh known hosts using 'sudo mv ~/.ssh/known_hosts ~/.ssh/known_hosts_backup'
5. run in terminal: easypy <path>/tbj.py -testbed_file <path>/docker-env.yaml