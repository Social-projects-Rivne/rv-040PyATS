# rv-040PyATS
Short description

# Setup
### Prerequisites 
- Python [3.4 or higher](https://www.python.org/downloads/)
- Virtual environment [Virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Docker [install](https://docs.docker.com/install/)
- gns3 [install](https://docs.gns3.com/1QXVIihk7dsOL7Xr7Bmz4zRzTsJ02wklfImGuHwTlaA4/index.html)

### Setting up the project
- create new virtual env `mkvirtualenv pyats -p <path/to/python3>`
- activate the env by running `workon pyats`
- Install modules `pip install -r ~/<path to project>/requirements.pip`
- Clone repository [rv-40PyATS](https://github.com/Social-projects-Rivne/rv-040PyATS)  

# Libs
- lib [pyats-5.0.1](https://developer.cisco.com/docs/pyats/)
- lib [genie-3.1.0](https://pubhub.devnetcloud.com/media/pyats-packages/docs/index.html)
- lib [paramiko-2.4.0](https://docs.paramiko.org/en/2.4/)

## Code quality
Project supports code style inspections with [pycodestyle]() tool.
Run `pip install pycodestyle` to perform project code inspection using `pep8`.
 
## Run tests
- read readme.md in local directories.