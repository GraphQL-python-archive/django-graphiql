from setuptools import setup, find_packages

setup(
    name='django-graphiql',
    version='0.3.1.6',
    download_url='git@github.com:graphql-python/django-graphiql.git',
    packages=find_packages(),
    author='Syrus Akbary',
    author_email='me@syrusakbary.com',
    description='Integrate GraphiQL easily into your Django project',
    long_description=open('README.rst').read(),
    keywords='django graphiql graphql graphene graphql-core',
    url='http://github.com/graphql-python/django-graphiql',
    license='MIT',
    entry_points={
    },
    install_requires=['django>=1.7'],
    tests_require=[],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
)
