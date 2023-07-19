FROM ghcr.io/ezynook/superset/superset:v1

ENV SUPERSET_HOME /superset
ENV SECRET_KEY 'dataengineer'
ENV PYTHONPATH $SUPERSET_HOME:$PYTHONPATH

COPY ./script/softnix.sh /superset/softnix.sh

EXPOSE 8088


ENTRYPOINT [ "/superset/softnix.sh" ]