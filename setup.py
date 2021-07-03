from setuptools import setup

setup(name='left-pad', 
    version='0.1',
    description='left-pad Python Package for Flask', 
    url='https://github.com/ectoglasses/left-pad', 
    author='Caspar', 
    author_email='', 
    license='MIT', 
    packages=['left-pad'],
    package_dir={"left-pad": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=["cryptography"],
)
