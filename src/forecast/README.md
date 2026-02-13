# Forecast

## UV

```shell
uv init
uv add numpy matplotlib
uv export --format requirements.txt --output-file requirements.txt
```

## Apptainer

```shell
apptainer build Forecast.sif Apptainer.def
apptainer run Forecast.sif
```
