import os
import setuptools

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as file:
        return file.read()

install_requires = read("requirements.txt")
install_requires = install_requires.split("\n")
install_requires = list(filter(lambda x: x[0:1] != "#", install_requires))
print("install-requires:", install_requires)

setuptools.setup(
    name = "printb",
    version = "1.0.3",
    author = "Michael Moser",
    author_email = "moser.michael@gmail.com",
    description = ("printb is a wrapper for print/input built-ins, that swaps string directions for BIDI languages."),
    license = "MIT",
    keywords = "text processing, bidi languages",
    url = "https://github.com/MoserMichael/printb",
    package_dir={'': 'src'},
    packages=setuptools.find_packages("src"),
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing"
    ],
    python_requires='>=3.6',
)
