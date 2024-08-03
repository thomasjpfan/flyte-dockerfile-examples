from flytekit import task

image = "ghcr.io/thomasjpfan/flyte-micromamba-regular:0.0.4"


@task(container_image=image)
def compute() -> int:
    import pandas as pd

    df = pd.DataFrame({"a": [1, 2, 3, 4]})
    return df["a"].sum().item()
