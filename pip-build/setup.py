import os
import setuptools 

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setuptools.setup(
    name = "printb", 
    version = "0.0.2",
    author = "Michael Moser",
    author_email = "moser.michael@gmail.com",
    description = ("printb is a wrapper for print/input built-ins, that swaps string directions for BIDI languages."),
    license = "MIT",                                                               
    keywords = "text processing, bidi languages",
    url = "https://github.com/MoserMichael/printb",
    packages=setuptools.find_packages(),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing"
    ],
    python_requires='>=3.6',
)
