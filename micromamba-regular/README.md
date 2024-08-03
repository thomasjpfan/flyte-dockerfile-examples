# Micromamba with flytekit

This provides the best practices for building a Docker image that:

- Supports flytekit
- `micromamba` using `requirements.yaml` for dependencies

```bash
docker image build \
    --platform linux/amd64 \
    -t localhost:30000/flyte-micromamba-regular:0.0.4 \
    --push .
```
