# pdp-project

## About

This is a test project to pair with pdp

## Usage

See [pdp](https://github.com/scienceandhumanitylab/pdp) for instructions on installing and using pdp.

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

To run PDP, first re-scaffold folders that are not kept by git with `pdp scaffold`. See [pdp](https://github.com/scienceandhumanitylab/pdp) for details.

