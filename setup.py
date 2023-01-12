#!/usr/bin/env python
import os

from setuptools import find_namespace_packages
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md")) as f:
    long_description = f.read()

package_name = "dbt-buenavista"
package_version = "1.3.0"
description = """The buenavista adapter plugin for dbt (data build tool)"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Josh Wills",
    author_email="joshwills+dbt@gmail.com",
    url="https://github.com/jwills/dbt-buenavista",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-postgres~=1.3.0",
    ],
    extras_require={
        "duckdb": ["dbt-duckdb~=1.3.0"],
    },
)
