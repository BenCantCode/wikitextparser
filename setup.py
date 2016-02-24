from distutils.core import setup

setup(
    name='wikitextparser',
    version='0.7.3dev',
    description='A simple, purely python, WikiText parsing tool.',
    long_description=open('README.rst').read(),
    author='Dalba',
    author_email='dalba.wiki@gmail.com',
    url='https://github.com/irdb/wikitextparser',
    packages=['wikitextparser'],
    install_requires=['wcwidth'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
    license='GNU General Public License v3 (GPLv3)',
)
