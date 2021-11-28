from setuptools import find_packages, setup

setup(
    name="eloquent_matsumoto",
    version="0.1",
    description="My ML package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
