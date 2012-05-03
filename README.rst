CherryPy on 30loops
===================

This is a very simple Hello World app to demonstrate how to run CherryPy apps
on 30loops.

App creation
------------

The CherryPy app will be run by Gunicorn as a regular WSGI app. Therefore we
specify the WSGI entrypoint, and create a WSGI flavored app:

``thirty create app helloworld git://github.com/bastichelaar/30loops-cherrypy.git --flavor wsgi --wsgi-entrypoint wsgi:application``

Then deploy:

``thirty deploy helloworld``

And you're done!
