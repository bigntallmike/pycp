from setuptools import setup
import os
import sys
import pycp


setup(name='pycp',
      version="8.0.1",
      description='cp and mv with a progressbar',
      author=" Dimitr Merejkowsky",
      url='http://github.com/dmerejkowsky/pycp',
      packages=['pycp'],
      license='COPYING',
      install_requires=[
          "attrs",
          "python-cli-ui",
      ],
      entry_points={
          "console_scripts": [
              "pycp = pycp.main:main",
              "pymv = pycp.main:main",
            ]
      },
      classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Shells",
      ],
      )
