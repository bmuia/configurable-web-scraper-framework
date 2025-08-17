from setuptools import setup, find_packages

setup(
    name="configurable_web_scraper",
    version="0.1.0",
    description="A configurable web scraper framework",
    author="Belam Muia",
    packages=find_packages(),  
    install_requires=[
        "requests>=2.31.0",  
    ],
    python_requires='>=3.10',
)
