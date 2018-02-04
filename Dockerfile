ARG JUPYTERHUB_VERSION
FROM jupyterhub/jupyterhub:$JUPYTERHUB_VERSION
MAINTAINER dtaniwaki

RUN pip install jupyterhub-dummyauthenticator==0.3
COPY ucrspawner /tmp/ucrspawner/ucrspawner
COPY setup.py /tmp/ucrspawner/setup.py
RUN cd /tmp/ucrspawner \
  && pip install . \
  && rm -fr /tmp/ucrspawner
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

ENV JUPYTERHUB_API_IP=<placeholder>
ENV JUPYTERHUB_API_PORT=<placeholder>
ENV NOTEBOOK_IMAGE=<placeholder>
ENV MARATHON_HOST=<placeholder>
ENV MESOS_USER=<placeholder>

ARG JUPYTERHUB_UID=1000

RUN adduser --system --no-create-home --uid $JUPYTERHUB_UID jupyterhub
RUN chown -R jupyterhub /srv/jupyterhub
USER jupyterhub
