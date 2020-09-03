from setuptools import setup

install_requires = [
    'matplotlib'
    ]

setup(
    name='geoplot',
    version=0.1,
    description="""
        geoplot is a Python module that expands TASplot, from John A.
        Stevenson (@volcano01010), it has the original functions of 
        tasplot, as well as new ones, from classical geochemistry
        diagrams""",
    license='MIT',
    author='Eduardo Valentin',
    author_email='eduardovalentindossantos@gmail.com',
    install_requires=install_requires,
    packages=['geoplot'],
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
