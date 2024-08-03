FROM python:3.11-slim-buster

RUN id -u flytekit || useradd --create-home --shell /bin/bash flytekit
RUN chown -R flytekit /root && chown -R flytekit /home

RUN --mount=type=cache,sharing=locked,mode=0777,target=/root/.cache/pip,id=pip \
    pip install poetry==1.8.3

ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_CACHE_DIR=/opt/poetry_cache \
    POETRY_NO_INTERACTION=1 \
    # Flyte specific env variables
    FLYTE_SDK_RICH_TRACEBACKS=0 \
    PYTHONPATH=/root

WORKDIR /opt/poetry
RUN --mount=type=bind,target=pyproject.toml,src=pyproject.toml \
    --mount=type=bind,target=poetry.lock,src=poetry.lock \
    --mount=type=bind,target=poetry.lock,src=poetry.lock \
    poetry install

ENV PATH="/opt/poetry/.venv/bin:$PATH"

USER flytekit
WORKDIR /root
