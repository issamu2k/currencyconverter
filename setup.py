from setuptools import setup

"""
run from project folder:
python setup.py sdist bdist_wheel
or
pip wheel .
"""

setup(
    use_scm_version=True,
)
