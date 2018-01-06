from setuptools import setup, find_packages

setup(
    name='scikit-groups',
    version='0.8',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An package for constructing finite abelian groups',
    long_description=open('README.txt').read(),
    install_requires=[],
    url='https://github.com/smeths/scikit-groups',
    author='John Smethurst & Paul Bradley',
)
