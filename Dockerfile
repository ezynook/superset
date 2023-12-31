FROM ghcr.io/ezynook/superset/superset:v1

ENV SUPERSET_HOME /superset
ENV SECRET_KEY 'cGFzaXR5Lgo='
ENV PYTHONPATH $SUPERSET_HOME:$PYTHONPATH

RUN apt-get update -y \
    && apt-get install -y net-tools
COPY ./script/softnix.sh /superset/softnix.sh
RUN chmod +x /superset/softnix.sh
EXPOSE 8088

ENTRYPOINT [ "/superset/softnix.sh" ]