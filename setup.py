from setuptools import setup, find_packages
from PycordPaginator import __version__

setup(
    name="PycordPaginator",
    license="MIT",
    version=__version__,
    description="paginator using pycord_components",
    author="SpaceDEV",
    author_email="support@spacedev.space",
    url="https://github.com/SpaceDEVofficial/pycord-paginator",
    packages=find_packages(),
    long_description=open('README.md', 'rt', encoding='UTF8').read(),
    long_description_content_type="text/markdown",
    keywords=["discord.py", "paginaion", "button", "components", "discord_components","pycord","py-cord"],
    python_requires=">=3.6",
    install_requires=["py-cord","pycord-components"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)