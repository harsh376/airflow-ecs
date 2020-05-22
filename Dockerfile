FROM puckel/docker-airflow:1.10.9

USER root

COPY script/entrypoint.sh /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_USER_HOME}/airflow.cfg

RUN chown -R airflow: ${AIRFLOW_USER_HOME}

USER airflow

WORKDIR ${AIRFLOW_USER_HOME}

# webserver
EXPOSE 8080
# worker
EXPOSE 5555
# flower
EXPOSE 8793

ENTRYPOINT ["/entrypoint.sh"]

# the first arg that `entrypoint.sh` gets called with.
# https://docs.docker.com/engine/reference/builder/#understand-how-cmd-and-entrypoint-interact
CMD ["webserver"]
