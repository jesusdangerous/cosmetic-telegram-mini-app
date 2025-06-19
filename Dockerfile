FROM ubuntu:latest
LABEL authors="aleks"

ENTRYPOINT ["top", "-b"]