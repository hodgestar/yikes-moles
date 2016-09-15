from setuptools import setup, find_packages

setup(
    name="yikes-moles",
    version="1.0.0",
    url='http://github.com/hodgestar/yikes-moles',
    license='BSD',
    description="Mole whacking on a grand scale.",
    long_description=open('README.rst', 'r').read(),
    author='Simon Cross',
    author_email='hodgestar+moles@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame-cffi',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment',
    ],
)
