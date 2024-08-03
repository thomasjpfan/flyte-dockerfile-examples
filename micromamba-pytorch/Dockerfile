#syntax=docker/dockerfile:1.9

FROM mambaorg/micromamba:1.5.8-bookworm-slim AS micromamba

FROM debian:bookworm-slim AS base

RUN id -u flytekit || useradd --create-home --shell /bin/bash flytekit
RUN chown -R flytekit /root && chown -R flytekit /home

ENV DEBCONF_NONINTERACTIVE_SEEN=true \
    DEBIAN_FRONTEND=noninteractive

# Add your APT dependencies here
RUN --mount=type=cache,sharing=locked,mode=0777,target=/var/cache/apt,id=apt \
    apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates
RUN update-ca-certificates

ENV SSL_CERT_DIR=/etc/ssl/certs \
    MAMBA_ROOT_PREFIX=/opt/micromamba \
    # Flytekit specific env
    FLYTE_SDK_RICH_TRACEBACKS=0 \
    PYTHONPATH=/root \
    # Optimistically set NVIDIA PATHs, NVIDIA device plugin for Kubernetes will
    # inject the NVIDIA driver into the container.
    PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:/opt/micromamba/envs/dev/bin:$PATH \
    LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64

COPY --from=micromamba /usr/bin/micromamba /usr/bin/micromamba

# Do not use micromamba lock files because the cache is already locked by docker
RUN micromamba config set use_lockfiles False
# Mount the requirements.yaml file and install with micromamba
RUN --mount=type=cache,sharing=locked,mode=0777,target=/opt/micromamba/pkgs,id=micromamba \
    --mount=type=cache,sharing=locked,mode=0777,target=/root/.cache/pip,id=pip \
    --mount=type=bind,target=requirements.yaml,src=requirements.yaml \
    micromamba env create -n runtime -f requirements.yaml

USER flytekit
WORKDIR /root
ENTRYPOINT [ "micromamba", "run", "-n", "runtime"]
