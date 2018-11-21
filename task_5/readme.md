# build
docker build -t my-tests .
# run
docker run -it -e word=myword123 my-tests
# or
docker run -it --env-file <path to file>/env.list my-tests