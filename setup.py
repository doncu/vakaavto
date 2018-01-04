import glob

from pip.req import parse_requirements
from setuptools import setup
from setuptools import find_packages


setup(
    name='Vaka-Avto',
    version='0.0.1',
    author="Ivan Krivosheev, Semen Doncu",
    author_email="py.krivosheev@gmail.com, doncusemen@gmail.com",
    description="Site for Vaka-Avto",
    url='http://vaka-avto.ru/',
    zip_safe=False,
    python_requires='>=3.4',
    packages=find_packages(),
    include_package_data=True,
    data_files=(
        ('static', glob.glob('static/**/*', recursive=True) + ['static/robots.txt']),
        ('configs', ['etc/uwsgi.ini', 'etc/supervisord.conf']),
    ),
    install_requires=[str(ir.req) for ir in parse_requirements('requirements.txt', session='hack')]
)
