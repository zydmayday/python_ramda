from os.path import abspath, dirname, join

from setuptools import find_packages, setup

# Fetches the content from README.md
# This will be used for the "long_description" field.
with open(join(dirname(abspath(__file__)), "README.md"), encoding='utf-8') as f:
  README_MD = f.read()

setup(
    # The name of your project that we discussed earlier.
    # This name will decide what users will type when they install your package.
    # In my case it will be:
    # pip install pydash-arnu515
    # This field is REQUIRED
    name="python_ramda",

    # The version of your project.
    # This field is REQUIRED
    version="0.8.0",

    # The packages that constitute your project.
    # For my project, I have only one - "pydash".
    # Either you could write the name of the package, or
    # alternatively use setuptools.findpackages()
    #
    # If you only have one file, instead of a package,
    # you can instead use the py_modules field instead.
    # EITHER py_modules OR packages should be present.
    packages=find_packages(exclude="tests"),

    # The description that will be shown on PyPI.
    # Keep it short and concise
    # This field is OPTIONAL
    description="A small clone of ramda",

    # The content that will be shown on your project page.
    # In this case, we're displaying whatever is there in our README.md file
    # This field is OPTIONAL
    long_description=README_MD,

    # Now, we'll tell PyPI what language our README file is in.
    # In my case it is in Markdown, so I'll write "text/markdown"
    # Some people use reStructuredText instead, so you should write "text/x-rst"
    # If your README is just a text file, you have to write "text/plain"
    # This field is OPTIONAL
    long_description_content_type="text/markdown",

    # The url field should contain a link to a git repository, the project's website
    # or the project's documentation. I'll leave a link to this project's Github repository.
    # This field is OPTIONAL
    url="https://github.com/zydmayday/python_ramda",

    # The author name and email fields are self explanatory.
    # These fields are OPTIONAL
    author_name="zydmayday",
    author_email="zydmayday@gmail.com",

    # Classifiers help categorize your project.
    # For a complete list of classifiers, visit:
    # https://pypi.org/classifiers
    # This is OPTIONAL
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],

    # Keywords are tags that identify your project and help searching for it
    # This field is OPTIONAL
    keywords="functional programming, ramda",

    # For additional fields, check:
    # https://github.com/pypa/sampleproject/blob/master/setup.py
)
