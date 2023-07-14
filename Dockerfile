FROM rawimage:latest

ENV SUPERSET_HOME /superset
ENV SECRET_KEY 'dataengineer'
ENV PYTHONPATH $SUPERSET_HOME:$PYTHONPATH

EXPOSE 8088


ENTRYPOINT [ "/superset/softnix.sh" ]