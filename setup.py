from setuptools import setup, find_packages

setup(
    name="DGXutils",
    version="0.1",
    packages=find_packages(),
    install_requires=["torch", "numpy", "pynvml"],
    author="Peter I. Kruse, John Lagergren",
    author_email="peter.ingraham.kruse@gmail.com",
    description="Utility functions for the DGX computing cluster",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pikruse/DGXutils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)