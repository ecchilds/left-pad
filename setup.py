from setuptools import setup, find_packages

packages = find_packages(exclude=['ez_setup', 'tests', 'tests.*'])
packages.append("leftpad")

setup(name="leftpad", 
    version='0.1',
    description='left-pad Python Package for Flask', 
    url='https://github.com/ectoglasses/left-pad', 
    author='Caspar', 
    author_email='', 
    license='MIT', 
    packages=packages,
    package_dir={"leftpad": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=["cryptography"],
)
