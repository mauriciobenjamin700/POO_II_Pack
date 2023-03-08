from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='data_formatada',
    version='1.0',
    license='MIT License',
    author='Mauricio Benjamin da Rocha & Pedro Antonio Vital de Sousa Carvalho',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='mauriciobenjamin700@gmail.com',
    keywords='datas tempo',
    description=u'Pacote para trabalhar com datas e horas no Brasil',
    packages=['data_formatada'],
    install_requires=[''],)