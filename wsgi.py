import cherrypy

class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

application = cherrypy.tree.mount(HelloWorld(), '')
