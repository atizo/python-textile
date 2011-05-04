from setuptools import setup, find_packages

version = '2.1.5'

setup(
    name='python-textile',
    version=version,
    description='Textile processing for python.',
    author='Chris Drackett',
    author_email='chris@chrisdrackett.com',
    url='http://github.com/chrisdrackett/python-textile',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1',
        'Environment :: Web Environment',
        'Intended Audience :: Developers :: Designers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='textile,text',
    test_suite = 'nose.collector',
    tests_require = ['nose'],
    include_package_data=True,
    zip_safe=False,
)
