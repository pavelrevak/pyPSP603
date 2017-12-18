"""A setup tools based setup module.
"""

import setuptools

setuptools.setup(name='pypsp',
    version='0.1',
    author='Tymm Twillman, Pavel Revak',
    author_email='tymmothy@gmail.com, pavel.revak@gmail.com',
    description='GW-Instek PSP power supply control module',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
    py_modules=[
        'psp'
    ],
)
