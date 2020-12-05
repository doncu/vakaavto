import glob
import pathlib
import collections

import setuptools


def get_recursive_files(src, dst):
    data_files = collections.defaultdict(list)
    for path in glob.glob('{}/**/*'.format(src), recursive=True):
        path_obj = pathlib.Path(path)
        if path_obj.is_file():
            new_path = (dst, ) + path_obj.parent.parts[1:]
            dirname = pathlib.Path(*new_path)
            data_files[str(dirname)].append(path)

    return tuple(data_files.items())


setuptools.setup(
    name='vakaavto',
    version='2.0.10',
    author="Ivan Krivosheev, Semen Doncu",
    author_email="py.krivosheev@gmail.com, doncusemen@gmail.com",
    description="Site for Vaka-Avto",
    url='http://vakaavto.ru/',
    zip_safe=False,
    python_requires='>=3.4',
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=get_recursive_files('etc', 'etc') + get_recursive_files('static', 'static'),
    entry_points='''
        [console_scripts]
        vakaavto=vakaavto:cli
    ''',
    install_requires=[
        "flask==0.12.2",
        "flask-admin==1.5.0",
        "uwsgi==2.0.19",
        "setuptools==36.7.2",
        "sqlalchemy==1.1.15",
        "covador==0.9.17",
        "pillow==2.7.0",
    ]
)
