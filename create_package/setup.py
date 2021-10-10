import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="rateme",
    version="0.1.1",
    author='banderlog',
    author_email="b.a.kabakov@gmail.com",
    url="https://github.com/banderlog/rateme",
    license='MIT',
    description="RateMe is a neural network that allows you to recognize gestures of thumb up and thumb down",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['rateme'],
    package_data={'rateme': ['*.weights', '*.cfg']},
    install_requires=['numpy', 'opencv-python-inference-engine>=2021-10-10'],
)
