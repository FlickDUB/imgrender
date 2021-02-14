import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imgrender-windows",
    version="0.0.3b",
    author="Vasiliev Danil",
    author_email="vasiljev.danil@gmail.com",
    description="Python terminal image renderer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlickDUB/imgrender-windows",
    packages=setuptools.find_packages(),
    install_requires=[
        'Colr==0.9.1',
		'numpy==1.19.4',
		'Pillow==8.0.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'imgrender = imgrender:main',
        ],
    },
    python_requires='>=3.6',
)
