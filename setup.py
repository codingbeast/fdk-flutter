from setuptools import setup, find_packages

setup(
    name="fdk",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'fdk = fdk.fdk:main',
        ],
    },
)
