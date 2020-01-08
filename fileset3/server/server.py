#!/usr/bin/python3

import logging
import signal
from tornado import httpserver
from tornado import ioloop
from tornado import web

__all__ = (
    'FilesetHandler',
    'run',
)


class FilesetHandler(web.RequestHandler):
    """Base handler for fileset."""

    def get(self):
        self.set_header('Content-Type', 'text/plain')
        self.write('hello world\n')
        for key in self.request.headers:
            val = self.request.headers[key]
            self.write('{}: {}\n'.format(key, val))


def create_app():
    """Creates a tornado web application."""
    app = web.Application(handlers=[
        (r'/', FilesetHandler),
    ])
    return app


def run(port: int = 8080):
    """Starts the fileset3 server."""
    current_ioloop = ioloop.IOLoop.current()

    # Start the web server.
    app = create_app()
    logging.info('starting server: localhost:{}'.format(port))
    server = httpserver.HTTPServer(app)

    try:
        server.listen(port)
        current_ioloop.start()
    except KeyboardInterrupt:
        pass
    finally:
        current_ioloop.stop()
