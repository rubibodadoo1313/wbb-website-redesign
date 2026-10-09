"""Local preview that serves the site the way Netlify does.

The pages are flat .html files but their public addresses have no extension,
which `python -m http.server` and VS Code's Live Server both get wrong: they
404 on /activities. GitHub Pages resolves /activities to activities.html, so
this does the same, and clicking around locally matches the deployed site.

GitHub Pages serves .html addresses too rather than redirecting them away,
and it has no redirect rules to change that, so neither does this.

    python dev-server.py [port]        # default 5173
"""

import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.dirname(os.path.abspath(__file__))


class CleanURLHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split('?', 1)[0].split('#', 1)[0]

        # /activities has no file behind it; activities.html does
        if path != '/' and '.' not in path.rsplit('/', 1)[-1]:
            candidate = os.path.join(ROOT, path.lstrip('/').replace('/', os.sep) + '.html')
            if os.path.isfile(candidate):
                self.path = path + '.html'

        return SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        # a preview that serves yesterday's CSS is worse than no preview
        self.send_header('Cache-Control', 'no-store')
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5173
    os.chdir(ROOT)
    print('Serving %s on http://localhost:%d (Ctrl+C to stop)' % (ROOT, port))
    ThreadingHTTPServer(('127.0.0.1', port), CleanURLHandler).serve_forever()
