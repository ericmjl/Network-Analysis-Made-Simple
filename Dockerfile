# For use with both Dokku and Binder
FROM continuumio/miniconda3


# We isolate the conda environment setup step
# because it is time consuming and a bit of a RAM hog.
ADD environment.yml /environment.yml
RUN conda env create -f /environment.yml
RUN rm /environment.yml

# We put the custom source installation steps here
# and not in the `environment.yml` file
# to prevent Docker from rebuilding the environment
# each time the source and notebooks change (which they will).
# This is extremely time consuming and expensive during the build.
ADD nams /tmp/setup/nams
ADD setup.py tmp/setup/setup.py
WORKDIR /tmp/setup
RUN python setup.py install
RUN rm -rf /tmp/setup

# Now we add the repository to the Docker container
ADD . /nams
WORKDIR /nams
ENV PATH="/opt/conda/envs/nams/bin:${PATH}"
RUN python -m ipykernel install --name nams

# Build docs in the container in this step
RUN mkdocs build

# Run Python web server to serve up static files
EXPOSE 80
ENTRYPOINT python -m http.server 80 -d site/
