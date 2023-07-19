FROM ghcr.io/ezynook/superset/superset:v1

ENV SUPERSET_HOME /superset
ENV SECRET_KEY 'dataengineer'
ENV PYTHONPATH $SUPERSET_HOME:$PYTHONPATH

RUN apt-get update -y && apt-get install -y net-tools

COPY ./script/softnix.sh /superset/softnix.sh

EXPOSE 8088


ENTRYPOINT [ "/superset/softnix.sh" ]