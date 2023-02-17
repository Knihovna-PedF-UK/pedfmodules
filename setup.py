from setuptools import setup

setup(
  name='PedF Modules',
  version='0.1.0',
  author='Michal Hoftich',
  author_email='michal.hoftich@pedf.cuni.cz',
  packages=['pedfmodules'],
  # scripts=['bin/script1','bin/script2'],
  url='https://github.com/Knihovna-PedF-UK/pedfmodules',
  license='LICENSE',
  description='Supporting modules for PedF UK Library',
  long_description=open('README.md').read(),
  install_requires=[
      "pandas",
      "pymarc",
  ],
)
