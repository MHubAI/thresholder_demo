from setuptools import setup

setup(
  name='thresholder',
  version='1.0',
  description='A package for thresholding images',
  author='Leonard Nuernberg',
  author_email='lnuernberg@bwh.harvard.edu',
  url='https://github.com/mhubai/demo_thresholder',
  packages=['thresholder'],
  install_requires=[
    'SimpleITK>=2.3.0'
    'argparse>=1.4.0'
  ],
  entry_points={
    'console_scripts': [
      'thresholder=thresholder.main:main',
    ],
  },
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)