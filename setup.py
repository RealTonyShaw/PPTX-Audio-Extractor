import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PPTX-Audio-Extractor',
    version='0.1',
    author='Chell',
    author_email='tonyshaw123@hotmail.com',
    description='Extract audios from .pptx files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RealTonyShaw/PPTX-Audio-Extractor",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    install_requires=[
        'click'
    ]
)
