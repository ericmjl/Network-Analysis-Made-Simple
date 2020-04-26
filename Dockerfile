# For use with both Dokku and Binder
FROM continuumio/miniconda3


# Add our code
ADD . /opt/webapp/
WORKDIR /opt/webapp

# Install packages
RUN conda env create -f environment.yml
RUN conda activate nams

RUN which python
RUN python -m ipykernel install --nams

# Diagnostic
RUN which mkdocs
RUN mkdocs build

RUN which python


# Grab requirements.txt.
# ADD ./webapp/requirements.txt /tmp/requirements.txt
# Install dependencies
# RUN pip install -qr /tmp/requirements.txt
# RUN conda install scikit-learn
# CMD gunicorn --bind 0.0.0.0:$PORT wsgi
