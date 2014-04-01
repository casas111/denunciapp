

import cherrypy

from modules.main.main_resource import *


if __name__ == '__main__':

    cherrypy.tree.mount(
        mainDenunciappResource(), '/main',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()




