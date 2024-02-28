from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_thingsboard_iot/__init__.py
from erpnext_thingsboard_iot import __version__ as version

setup(
	name="erpnext_thingsboard_iot",
	version=version,
	description="Thingsboard integration for ERPNext",
	author="VIIS IoT Solution",
	author_email="baonguyen2409@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
