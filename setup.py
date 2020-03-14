import setuptools


setuptools.setup(
    name='PPTX-Audio-Extractor',
    version='0.1',
    author='Chell',
    author_email='tonyshaw123@hotmail.com',
    description='A gadget to extract audios inserted into .pptx files.',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'click'
    ]
)
