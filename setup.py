import setuptools

# you want to read the README file.
with open("README.md", "r") as f:
    long_description = f.read()

# package version:
__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "SoogeunParkValcon"
AUTHOR_EMAIL = "soogeun.park@valcon.com"
SRC_REPO = "TextSummarizer"

# local package setup: the following code finds the constructor file and installs the package

setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A small package for text summarization, using NLP",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir = {"": "src"}, 
    packages=setuptools.find_packages(where="src")
)