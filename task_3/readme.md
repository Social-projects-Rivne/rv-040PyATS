#up vagrant VM
    from: "Vagrantfile"

#util to copy files

    pip install paramiko
    pip install scp
    
# run test:
    easypy conn_job.py -testbed_file testbed.yaml
