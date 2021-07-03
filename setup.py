from setuptools import setup, find_packages

packages = find_packages(exclude=['ez_setup', 'tests', 'tests.*'])
packages.append("left-pad")

setup(name='left-pad', 
    version='0.1',
    description='left-pad Python Package for Flask', 
    url='https://github.com/ectoglasses/left-pad', 
    author='Caspar', 
    author_email='', 
    license='MIT', 
    packages=packages,
    package_dir="src",
    include_package_data=True,
    zip_safe=False,
    install_requires=["cryptography"],
)
