from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_integration_nacex/__init__.py
from erpnext_integration_nacex import __version__ as version

setup(
	name="erpnext_integration_nacex",
	version=version,
	description="Module to integrate shipments with Nacex delivery company",
	author="TORRMAN",
	author_email="info@torrman.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
