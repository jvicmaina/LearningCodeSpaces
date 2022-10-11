# devcontainer-python-template
Template repository for a Python project using Devcontainers. Fork this repository or use it as a template to get a fully functional devcontainer for your Python project.

## Container details

* Uses Python 3.10 (but allows other variants)
* Uses Debian Bullseye as the base OS
* Creates a Virtualenv in `/home/vscode/venv`
* Relies on a `requirements.txt` to install libraries in the virtual environment

## VSCode details

* Enables Pylance with the Python extension
* Installs and enables `flake8`. Other extensions are 100% allowed
* Runs a `python setup.py develop` which installs the project in the virtualenv

## Possible errors

* A missing `requirements.txt` file
* A missing `setup.py` file or no Python files to install

## GitHub Actions ready

* Uses a workflow for linting the included `Dockerfile`
