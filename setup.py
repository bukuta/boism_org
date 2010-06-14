import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
import sys

install_requires = [
    'django==1.1.2',
    'django-debug-toolbar==0.7.0',
    'South',
    'recaptcha-client',
    'markdown2',
    'html5lib',
    'python-openid',
    'django-keyedcache',
]
WIN_PLATFORMS = ('win32', 'cygwin',)
if sys.platform not in WIN_PLATFORMS:
    install_requires.append('mysql-python')

setup(
    name = "askbot",
    version = "0.6.0",
    packages = find_packages(),
    author = 'Evgeny.Fadeev',
    author_email = 'evgeny.fadeev@gmail.com',
    license = 'GPLv3',
    keywords = 'forum, community, wiki, Q&A',
    url = 'http://askbot.org',
    include_package_data = True,
    install_requires = install_requires,
    long_description = """Open Source Question and Answer forum.
    Based on CNPROG project by Mike Chen and Sailing Cai, project
    inspired by StackOverflow.
    """,
)

if sys.platform in WIN_PLATFORMS:
    print 'ATTENTION!! please install windows binary mysql-python package'
    print 'at http://www.codegood.com/archives/4'
