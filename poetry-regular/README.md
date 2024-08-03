# poetry with flytekit

This provides the best practices for building a Docker image that:

- Supports flytekit
- `poetry` for dependency management

```bash
docker image build \
    --platform linux/amd64 \
    -t localhost:30000/flyte-poetry-regular:0.0.3 \
    --push .
```
