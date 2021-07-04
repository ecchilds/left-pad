from setuptools import setup, find_packages

packages = find_packages()
packages.append("leftpad")

setup(name="leftpad", 
    version='1.16',
    description='left-pad Python Package for Flask', 
    url='https://github.com/ectoglasses/left-pad', 
    author='Caspar', 
    author_email='', 
    license='MIT', 
    packages=packages,
    package_dir={"leftpad": "src/leftpad"},
    package_data={"leftpad": ["backend/*.txt", "backend/datastore.py"]},
    include_package_data=True,
    zip_safe=False,
    install_requires=["cryptography"],
)
