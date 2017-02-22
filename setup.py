from setuptools import setup, find_packages

setup(
    name="pycell",
    packages=['pycell'],
    version="0.1",
    description="A Hydrogen code cell executor",
    author='Nils Werner',
    author_email='nils.werner@gmail.com',
    url='https://github.com/nils-werner/pycell',
    include_package_data=True,
    entry_points={'console_scripts': ['pycell = pycell.__main__:main']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ]
)
