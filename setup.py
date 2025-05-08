from setuptools import setup, find_packages

def get_version():
    with open("chumpy/version.py") as f:
        for line in f:
            if line.startswith("version"):
                return line.split("=")[1].strip().strip("'\"")

setup(
    name='chumpy',
    version=get_version(),
    packages=find_packages(),
    author='Matthew Loper',
    author_email='matt.loper@gmail.com',
    url='https://github.com/mattloper/chumpy',
    description='chumpy',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux'
    ],
)

