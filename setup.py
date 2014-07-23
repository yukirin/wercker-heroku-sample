from setuptools import setup, find_packages

setup(
    name='werckerherokusample',
    version='0.1.0',
    description='Python Package',
    author='yukirin',
    author_email='standupdown@gmail.com',
    url='https://github.com/yukirin/wercker-heroku-sample',
    license='MIT',
    keywords=['python'],
    zip_safe=False,
    install_package_data=True,
    packages=find_packages(),
    platforms=['Linux'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['tornado'],
)
