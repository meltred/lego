<div align="center">
    <img src="https://github.com/meltred/lego/assets/82411321/36de7d4d-9eed-4685-899b-39e8f863a665" alt="Lego Text Logo" />
</div>

# Lego - Python Bootstrapper for AI

<a href="https://github.com/meltred">
    <img src="https://github.com/meltred/lego/assets/82411321/adc2d7cf-2e3b-47f8-b25f-27d03adbf9aa" alt="Open Sourced by Meltred" />
</a>

### Project Setup

#### Python can use `pyproject.toml` to list dependencies instead of `requirements.txt` file

Old way was to use `requirements.txt` but its no long recommended.

New way is to use a dependencies manager

## `Poetry` - The Dependencies manager

Link: https://python-poetry.org/

Installation: https://python-poetry.org/docs/#installing-with-pipx

Installation using `Pipx` - **pipx** is used to install global cli tools with isolating then in virtual environments.

```bash
sudo pip install pipx
```

```bash
pipx install poetry
# upgrade and uninstall is also supported
```

## Using `poetry`

Init a new project

```bash
poetry init
```

Add Dependencies

```bash
poetry add pytest
```

Add Dependencies with version

```bash
poetry add requests@2.12.1
```

[Default] Add Dependencies with latest version un-till major change

```bash
poetry add requests^2.12.1
```

> This will try to install more newer version but not `3.x.x`

Add Dependencies upto latest minor version

```bash
poetry add requests~2.12.1
```

> This will install `2.12.5`

Show all the dependencies

```bash
poetry show
# poetry show requests
```

Remove dependencies

```bash
poetry remove pytest
```

Install Dependencies for new project

```bash
poetry install
```

## Virtual Environment

`poetry` can create virtual environment for running the application

Spawn a new shell

```bash
poetry shell
```

## Versioning

```bash
poetry version patch
# `x.y.z` this will bump z
```

```bash
poetry version minor
# `x.y.z` this will bump y
```

```bash
poetry version major
# `x.y.z` this will bump x
```

## Packaging

```bash
poetry package
# need pypy credentials
```
