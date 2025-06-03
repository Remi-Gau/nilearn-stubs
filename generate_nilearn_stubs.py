import subprocess
from pathlib import Path

from rich import print

# Root directory of the nilearn source code
NILEARN_SRC_DIR = Path("nilearn-stubs")

# List of modules to explicitly exclude
EXCLUDE_LIST = [
    "tests",
]

# List of modules to explicitly include (leave empty to include all except excluded)
INCLUDE_LIST = ["nilearn._utils"]


def get_traced_modules() -> list[str]:
    """Return a list of modules traced by MonkeyType that are in the nilearn package."""
    result = subprocess.run(["monkeytype", "list-modules"], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Failed to run monkeytype list-modules: {result.stderr}")
    return [line.strip() for line in result.stdout.splitlines() if line.startswith("nilearn.")]


def should_include(module: str) -> bool:
    exclude = any(x in module for x in EXCLUDE_LIST) if EXCLUDE_LIST else False
    if exclude:
        return False
    if not INCLUDE_LIST:
        return True
    return any(x in module for x in INCLUDE_LIST)


def generate_stub(module: str):
    """Generate stub for a module using monkeytype and write to correct .pyi path."""
    module_path = NILEARN_SRC_DIR / Path(module.replace(".", "/").replace("nilearn/", "")).with_suffix(".pyi")
    module_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        print(f"Generating stub for {module} -> {module_path}")
        result = subprocess.run(["monkeytype", "stub", module], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Failed to generate stub for {module}: {result.stderr}")
            return
        if not result.stdout:
            print("nothing to write")
        with module_path.open("w", encoding="utf-8") as f:
            f.write(result.stdout)
    except Exception as e:
        print(f"Error processing {module}: {e}")


def main() -> None:
    modules = get_traced_modules()
    for module in modules:
        if should_include(module):
            generate_stub(module)
        else:
            print(f"Skipping module: {module}")


if __name__ == "__main__":
    main()
