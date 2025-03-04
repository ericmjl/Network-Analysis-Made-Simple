FROM ghcr.io/prefix-dev/pixi:0.40.0 AS build

WORKDIR /app
COPY pixi.lock /app/pixi.lock
COPY pyproject.toml /app/pyproject.toml
COPY nams /app/nams

RUN pixi install

RUN pixi run python -m ipykernel install --user --name nams

# Build docs in the container in this step
COPY mkdocs.yml /app/mkdocs.yml
COPY notebooks /app/notebooks
RUN pixi run build-docs

# Run Python web server to serve up static files
EXPOSE 80
ENTRYPOINT python -m http.server 80 -d site/
