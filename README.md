# nilearn-stubs: unofficial type stubs for nilearn

## Install

pip install -e '.[dev]'


## Run tests with monkeytype

For example on `nilearn/_utils`

```bash
monkeytype run -m pytest -n 20 -c pyproject.toml nilearn/nilearn/_utils
```

## List annotated modules

```bash
monkeytype list-modules
```

## Generate stub

For example on `nilearn/_utils/path_finding.py`

```bash
monkeytype stub nilearn._utils.path_finding > nilearn/_utils/path_finding.py
```

## TODO

### Public classees and functions

- [ ] nilearn-stubs/glm
- [ ] nilearn-stubs/maskers
- [ ] nilearn-stubs/decoding
- [ ] nilearn-stubs/decomposition
- [ ] nilearn-stubs/plotting
