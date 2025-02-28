from setuptools import setup

setup(
    name="formatik",
    version="0.1.0",
    packages=["formatik"],
    description="Add your description here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/formatik",
    install_requires=["matplotlib"],
    include_package_data=True,
)
