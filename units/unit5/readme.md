Based on the materials from "Build custom image" section, you have to configure rabbit.py test execution with easypy module
within a Docker container. To do this, you need to prepare a Docker image which will have configured a job's execution by default.
This image has to be pushed to your Docker hub account.
The word parameter has to be passed to the job via either CLI argument or a testbed file ( testbed	>	custom	>	word path).

# build
docker build -t my-tests .
# run with parametr (unit5)
docker run -it -v <local path>:/my-tests -e word=myword123 my-tests
# or
docker run -it -v <local path>:/my-tests --env-file <path to file>/env.list my-tests


# run with testbase file (unit5file)
docker run -it my tests
# or
docker run -it -v <local path>:/my-tests my tests
