from setuptools import setup

setup(
    name='Calculator',
    version='2.1',
    packages=['calc_2_1'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)