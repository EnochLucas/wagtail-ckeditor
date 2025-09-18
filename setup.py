from setuptools import setup, find_packages

setup(
    name="wagtail-ckeditor5",
    version="0.1.0",  # Change this as you go
    description="CKEditor 5 integration for Wagtail CMS",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Bright Bridge Web",
    author_email="services@brightbridgeweb.com",
    url="https://github.com/BrightBridgeWeb/wagtail-ckeditor5",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wagtail>=4.2.4",
        "Django>=4.1.3",  # or whatever your lower bound is
    ],
    classifiers=[
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 4",
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # or whatever you’re using
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)