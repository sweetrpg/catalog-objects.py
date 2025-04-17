from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="sweetrpg-catalog-objects",
    install_requires=[
        "sweetrpg-model-core",
        "sweetrpg-common",
    ],
    extras_require={},
)
