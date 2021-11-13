import toml

VERSION_TEMPLATE: str = (
    "[![PyPI](https://img.shields.io/pypi/v/{package_name})]"
    "(https://pypi.org/project/{package_name}/)"
)
STATUS_TEMPLATE: str = (
    "[![PyPI - Status](https://img.shields.io/pypi/status/{package_name})]"
    "(https://pypi.org/project/{package_name}/)"
)
PYTHON_VERSIONS_TEMPLATE: str = (
    "[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{package_name})]"
    "(https://pypi.org/project/{package_name}/)"
)
LICENSE_TEMPLATE: str = (
    "[![PyPI - License](https://img.shields.io/pypi/l/{package_name})]"
    "({repo}/blob/main/LICENSE)"
)

if __name__ == "__main__":
    with open("pyproject.toml", "r") as f:
        metadata = toml.load(f)

    package_name = metadata["tool"]["poetry"]["name"]
    repo = metadata["tool"]["poetry"]["repository"]

    print(
        VERSION_TEMPLATE.format(package_name=package_name),
        STATUS_TEMPLATE.format(package_name=package_name),
        PYTHON_VERSIONS_TEMPLATE.format(package_name=package_name),
        LICENSE_TEMPLATE.format(package_name=package_name, repo=repo),
        sep="\n",
    )
