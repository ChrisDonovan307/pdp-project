# PDP Project

## About

This is a test project to pair with PDP

## Usage

See [PDP](https://github.com/samzhang111/pdp) for instructions on installing and using PDP.

To use the test project, clone and set up with [uv](https://docs.astral.sh/uv/getting-started/installation/)

```sh
# install uv if needed:
curl -LsSf https://astral.sh/uv/install.sh | sh

# clone and install pdp
git clone https://github.com/ChrisDonovan307/pdp-project.git
cd pdp-project

# set up environment
uv sync
source .venv/bin/activate
```

To run PDP, first re-scaffold folders that are not kept by git.

```sh
pdp scaffold
pdp validate
pdp run task1
pdp run
pdp dagster dev
```

There is no convenient cleanup feature yet, but you can: 

- `pdp run --force` if everything is current
- `rm task*/output/*` to remove outputs
- `git reset --hard origin/main`

