from setuptools import setup
from version import VERSION

requires = ['BeautifulSoup==3.2.0']

try:
    import json
except ImportError:
    requires.append('simplejson>=2.0.9')

setup(
    name='episode-renamer',
    author='Stavros Korokithakis',
    author_email='stavros@korokithakis.net',
    version=VERSION,
    py_modules=['episoderenamer', 'version'],
    description='TV episode renamer',
    long_description="TV episode renamer SCRIPT",
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Video',
    ],
    install_requires=requires,
    entry_points = {
        'console_scripts':[
            'episoderenamer = episoderenamer:main'
        ]
    },
)
