# Micromamba with flytekit + PyTorch + NVIDIA CUDA

This provides the best practices for building a Docker image that:

- Supports flytekit
- `micromamba` using `requirements.yaml` for dependencies
- Installs PyTorch and CUDA with `micromamba`

```bash
docker image build \
    --platform linux/amd64 \
    -t localhost:30000/flyte-micromamba-pytorch:0.0.4 \
    --push .
```
