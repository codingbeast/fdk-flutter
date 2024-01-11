from setuptools import setup, find_packages

setup(
    name="fdk",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "mycolorlogger==0.8"
        ],
    entry_points={
        'console_scripts': [
            'fdk = fdk.fdk:main',
        ],
    },
)
