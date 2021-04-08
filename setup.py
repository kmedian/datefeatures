from setuptools import setup
import pypandoc


setup(name='datefeatures',
      version='0.3.0',
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
