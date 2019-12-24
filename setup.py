from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='ebay_api_zs',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kambag',
    author='Kamil Bagaviev',
    author_email='kbagaviev@mail.ru',
    install_requires=[
        'requests==2.22.0',
        'PyYAML==5.1',
    ],
    # include_package_data=True,
    zip_safe=False,
    entry_points={},
    test_suite='tests',
)
