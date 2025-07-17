# Gooop

## Build

```sh
protoc --python_out=gooop ./proto/person.proto
```

## Test

```sh
poetry run pytest
```

## Run

```sh
poetry env activate
python3 -m gooop
```
