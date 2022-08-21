from setuptools import setup,find_packages

setup(
    name='Noelle Browser',
    version='0.0.1',
    description='Noelle pembantu surfing',
    author='Airmax121',
    license='MIT',
    url='https://github.com/Airmax121/noelle_web',
    author_email='iqbal.agyan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'numpy',
    ],
)