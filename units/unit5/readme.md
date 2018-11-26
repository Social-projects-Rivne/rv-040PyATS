# build
docker build -t my-tests .
# run
docker run -it -v <local path>:/my-tests -e word=myword123 my-tests
# or
docker run -it -v <local path>:/my-tests --env-file <path to file>/env.list my-tests