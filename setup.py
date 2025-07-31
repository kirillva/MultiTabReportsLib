from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="MultiTabReportsLib",
    version="0.0.1",
    author="kirill.avtonomov",
    author_email="kirill.avtonomov@yandex.ru",
    description="Для формирования xlsx отчета из нескольких csv файлов.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kirillva/MultiTabReportsLib",
    packages=find_packages(),
    install_requires=["requests>=2.25.1"],
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="files speedfiles ",
    project_urls={"GitHub": "https://github.com/kirillva/MultiTabReportsLib"},
    python_requires=">=3.6",
)
