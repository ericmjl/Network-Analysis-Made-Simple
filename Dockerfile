# For use with both Dokku and Binder
FROM continuumio/miniconda3


# Add code to setup
ADD environment.yml /tmp/setup/

# Install packages
RUN conda env create -f environment.yml

# We put the custom source here
# and not install it in `environment.yml`
# to prevent Docker from rebuilding the environment
# each time the source changes.
# This is extremely time consuming and expensive during the build.
ADD nams /tmp/setup/nams
ADD setup.py tmp/setup/setup.py
WORKDIR /tmp/setup
RUN python setup.py install

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
