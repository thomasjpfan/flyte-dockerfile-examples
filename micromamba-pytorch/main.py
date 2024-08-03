from flytekit import task, Resources

image = "ghcr.io/thomasjpfan/flyte-micromamba-pytorch:0.0.4"


@task(container_image=image, requests=Resources(gpu="1"))
def cuda_is_available() -> bool:
    import torch

    return torch.cuda.is_available()
