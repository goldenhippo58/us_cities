from setuptools import setup, find_packages

setup(
    name='us_cities',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='A library for information about US cities',
    author='Z Kleck',
    author_email='zkleckner@gmail.com',
    url='https://github.com/goldenhippo58/us_cities',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_data={
        'us_cities': ['data.csv'],
    },
)
