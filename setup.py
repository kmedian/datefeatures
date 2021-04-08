from setuptools import setup
import pypandoc


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='datefeatures',
      version=get_version("datefeatures/__init__.py"),
      description='Feature engineering sklearn transformer for dates',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/kmedian/datefeatures',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['datefeatures'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.14.5',
          'scikit-learn>=0.20.0',
          'pandas>=0.23.4',
          'holidays>=0.9.9'],
      python_requires='>=3.6',
      zip_safe=True)
