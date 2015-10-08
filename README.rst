Django GraphiQL
===============

Django GraphiQL is a library for integrating `GraphiQL`_ inside your
Django project, so you can test your `GraphQL`_ schemas easily.

This library versioning go in partity with GraphiQL.

Installing
----------

For installing this library just run in your favorite shell:

.. code:: bash

    pip install django-graphiql

Configuring
-----------

In settings.py add ``'django_graphiql'`` into ``INSTALLED_APPS``, so it
will look like

.. code:: python

    INSTALLED_APPS = [
        # ...
        'django_graphiql',
        # ...
    ]

And then, add into your urls.py:

.. code:: python

    urlpatterns = [
        # Your other urls...
        url(r'^graphiql', include('graphiql.urls')),
    ]

.. _GraphiQL: https://github.com/graphql/graphiql
.. _GraphQL: https://github.com/graphql-python/graphql-core
