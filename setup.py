# describes project + files belonging to it
# packaging: 
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

# project installabel in venv with "pip install -e"
# tells pip to find setup.py in current directory
# also installs it in "editable" or "developement" mode 
# editable mode: can make changes to local code without re-installing (only if metadata like dependencies change)
# when istalled, project can be run from everywhere (not just flask-tutorial directory) with "flask --app flaskr run"

# observe project with pip list
