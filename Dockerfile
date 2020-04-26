# For use with both Dokku and Binder
FROM continuumio/miniconda3


# Add code to setup
ADD environment.yml /tmp/setup/
ADD nams /tmp/setup/nams
ADD setup.py tmp/setup/setup.py
WORKDIR /tmp/setup

# Install packages
RUN conda env create -f environment.yml
# RUN conda init bash
RUN which conda
ADD . /opt/webapp
WORKDIR /opt/webapp
ENV PATH="/opt/conda/envs/nams/bin:${PATH}"
RUN which python
RUN python -m ipykernel install --name nams

# Diagnostic
RUN which mkdocs
RUN mkdocs build

RUN which python

EXPOSE 80
ENTRYPOINT python -m http.server 80 -d site/


# Grab requirements.txt.
# ADD ./webapp/requirements.txt /tmp/requirements.txt
# Install dependencies
# RUN pip install -qr /tmp/requirements.txt
# RUN conda install scikit-learn
# CMD gunicorn --bind 0.0.0.0:$PORT wsgi
