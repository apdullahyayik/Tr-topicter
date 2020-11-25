from distutils.core import setup

setup(
    name='tr_topicter',
    packages=['tr_topicter'],
    version='0.0.1',
    license='MIT',
    description='Turkish topic detector using machine learning',
    author='Apdullah YAYIK',
    author_email='apdullahyayik@gmail.com',
    url='https://github.com/apdullahyayik',
    download_url='https://github.com/apdullahyayik/Tr-topicter/archive/v0.0.1.tar.gz',
    keywords=['Turkish domain detector', 'text classification', 'topic classification'],
    install_requires=['fasttext'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
