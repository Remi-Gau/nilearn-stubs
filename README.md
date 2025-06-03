# nilearn-stubs: unofficial type stubs for nilearn

## Install

pip install -e '.[dev]'


## Run tests with monkeytype

For example on `nilearn/_utils`

```bash
monkeytype run -m pytest nilearn/nilearn/_utils
```

## List annotated modules

```bash
monkeytype list-modules
```

## Generate stub

For example on `nilearn/_utils/path_finding.py`

```bash
monkeytype stub nilearn._utils.path_finding > nilearn/_utils/path_finding.pyi
```

### Several files at once

Use a script:

```bash
python generate_nilearn_stubs.py
```

## Add annotation to codebase

```bash
python maint_tools/apply_types.py _utils/bids.pyi
```
