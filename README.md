## Lego - Python Project Bootstrapper for AI

Using [Pipenv](https://pipenv.pypa.io/), `Pipenv` is also a Virtualization and Dependencies manager like `Poetry`

## Docs

Create a new Project

```bash
mkdir new_proj
# Pipenv can install dependencies without already having .lock file
```

Install 

```bash
pipenv install numpy
```

Running Program

```bash
pipenv run python .\lego\main.py
```

### Usage Examples:

Create a new project using Python 3.7, specifically:

```bash
pipenv --python 3.7
```

Remove project virtualenv (inferred from current directory):

```bash
pipenv --rm
```

Install all dependencies for a project (including dev):

```bash
pipenv install --dev
```

Create a lockfile containing pre-releases:

```bash
pipenv lock --pre
```

Show a graph of your installed dependencies:

```bash
pipenv graph
```

Check your installed dependencies for security vulnerabilities:

```bash
pipenv check
```

Install a local setup.py into your virtual environment/Pipfile:

```bash
pipenv install -e .
```

Use a lower-level pip command:

```bash 
pipenv run pip freeze
```


Commands:

  - `check`         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  - `clean`        Uninstalls all packages not specified in Pipfile.lock.
  - `graph`         Displays currently-installed dependency graph information.
  - `install`       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  - `lock`          Generates Pipfile.lock.
  - `open`          View a given module in your editor.
  - `requirements`  Generate a requirements.txt from Pipfile.lock.
  - `run`           Spawns a command installed into the virtualenv.
  - `scripts`       Lists scripts in current environment config.
  - `shell`         Spawns a shell within the virtualenv.
  - `sync`          Installs all packages specified in Pipfile.lock.
  - `uninstall`     Uninstalls a provided package and removes it from Pipfile.
  - `update`       Runs lock, then sync.
  - `upgrade`       Resolves provided packages and adds them to Pipfile, or (if no
                packages are given), merges results to Pipfile.lock
  - `verify`        Verify the hash in Pipfile.lock is up-to-date.


![legobadge](https://github.com/meltred/lego/assets/82411321/ba2e2850-6cf8-468e-817b-62692045c98e)
