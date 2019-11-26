import os
from setuptools import setup


setup(
    name='optprompt',
    version='0.2.2',
    author='Dylan Stephano-Shachter',
    author_email='dylan@theone.ninja',
    description='A prompting option parser',
    license='LGPL',
    url='https://github.com/dstathis/optprompt',
    packages=['optprompt'],
    # 3.2 Required for callable()
    python_requires='>=3.2',
    long_description=open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
    ).read(),
    long_description_content_type='text/markdown',
    install_requires=open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'requirements.txt')
    ).read().splitlines(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
