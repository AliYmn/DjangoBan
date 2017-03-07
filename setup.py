from distutils.core import setup

setup(
    name='DjangoBan',
    version='1.9.0',
    packages=['ban', 'ban.migrations'],
    url='https://github.com/AliYmn/DjangoBan',
    license='MIT',
    author='aliyaman',
    author_email='aliymn.db@gmail.com',
    description='Django User Ban Management ',
    download_url='https://github.com/AliYmn/DjangoBan',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
