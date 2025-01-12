import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "nlp_text_summarization_huggingface"
AUTHOR_USER_NAME = "smmaisam"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "muhammad.maisam@gmail.com"


setuptools.setup(
    name=SRC_REPO,                              # Package name
    version=__version__,                        # Package version
    author=AUTHOR_USER_NAME,                    # Author name
    author_email=AUTHOR_EMAIL,                  # Author email
    description="A small python package for NLP app",  # Short description
    long_description=long_description,          # Detailed description from README.md
    long_description_content="text/markdown",   # Format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # GitHub repository URL
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Bug tracker URL
    },
    package_dir={"": "src"},                    # Base directory for the source code
    packages=setuptools.find_packages(where="src")  # Finds all subpackages under "src"
)