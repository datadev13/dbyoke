from setuptools import setup, find_packages

setup(
    name="dbyoke",
    version="0.1.3",
    description="A library to unify database connections and drivers",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="datadev13",
    author_email="",
    url="https://github.com/datadev13/dbyoke",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[],
    extras_require={
        "postgresql": ["psycopg2-binary"],
        "mssql": ["pyodbc"],
        "oracle": ["oracledb"],
        "all": ["psycopg2-binary", "pyodbc", "oracledb"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Database",
    ],
    keywords="database connection drivers unification",
)