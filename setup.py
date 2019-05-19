import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="wunderground_pws",
    version="0.1",
    description="Small Python module for Weather Underground PWS APIs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://marcobuster.github.io/wundergroundpws-api",
    project_urls={
        "GitHub": "https://github.com/MarcoBuster/WUndergroundPWS-API",
        "Documentation": "https://marcobuster.github.io/wundergroundpws-api",
    },
    author="Marco Aceti",
    author_email="mail@marcoaceti.it",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["wunderground_pws"],
    install_requires=["requests", "simplejson"],
)
