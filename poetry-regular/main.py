from flytekit import task

image = "ghcr.io/thomasjpfan/flyte-poetry-regular:0.0.3"


@task(container_image=image)
def compute() -> int:
    import polars as pl

    df = pl.DataFrame({"a": [1, 2, 3]})
    return df.select(pl.col("*").sum()).item()
