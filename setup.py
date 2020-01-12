import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jetkiller",
    version="1.1.0",
    author="Arnaud-D",
    description="Enhance data visualizations using the \"jet\" colormap.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Arnaud-D/jetkiller-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["pillow", "numpy", "matplotlib"],
    entry_points={
        'console_scripts': [
            'jetkiller = jetkiller.__main__:main',
        ],
    }
)
