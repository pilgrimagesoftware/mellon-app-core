from setuptools import find_packages, setup

setup(
    name="mellon-app-core",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "flask",
        "mellon-common",
        "requests",
        "jsonpath-rw",
        "sentry-sdk",
        "python-dotenv",
        "pymongo",
        "prometheus-flask-exporter"
    ])
