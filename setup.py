import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


def get_version(root, rel_path):
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find the version string (`__version__`).")


setup(
    name="pyrocco",
    version=get_version(HERE, "pyrocco/__init__.py"),
    description="A Python CLI to add the Party Parrot to a custom background image.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="João Palmeiro",
    author_email="jm.palmeiro@campus.fct.unl.pt",
    url="https://github.com/joaopalmeiro/pyrocco",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    license="MIT",
    install_requires=["pillow"],
    python_requires=">=3.6, <=3.8",
    project_urls={
        "Bug Reports": "https://github.com/joaopalmeiro/pyrocco/issues",
        "Source": "https://github.com/joaopalmeiro/pyrocco",
    },
    entry_points={"console_scripts": ["pyrocco=pyrocco.cli:main"]},
    include_package_data=True,  # Accept all data files and directories matched by `MANIFEST.in`.
    package_data={
        "": ["data/mega/*.png"]
    },  # Specify additional patterns to match files that may or may not be matched by `MANIFEST.in` or found in source control.
)
