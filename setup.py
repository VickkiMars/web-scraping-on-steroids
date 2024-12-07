from setuptools import setup, find_packages
setup(
    name="visurf",
    version="0.1.0",
    author="Victor Umoren",
    author_email="victorumoreng@gmail.com",
    description="An AI-assisted web scraper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VickkiMars/web-scraping-on-steroids",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "transformers",
        "requests"
    ]
)