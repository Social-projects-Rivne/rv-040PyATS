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
