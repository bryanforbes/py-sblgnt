from setuptools import setup

setup(
    name="py-sblgnt",
    version="0.10",
    description="pip-installable MorphGNT/SBLGNT with Python API",
    license="MIT",
    url="https://github.com/morphgnt/py-sblgnt",
    author="James Tauber",
    author_email="jtauber@jtauber.com",
    extras_require={"typings": ["typing_extensions>=3.7.4"]},
    packages=["pysblgnt"],
    package_data={"": ["sblgnt/*.txt", "py.typed", "*.pyi"]},
)
