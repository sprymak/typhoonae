# -*- coding: utf-8 -*-
#
# Copyright 2009 Tobias Rodäbel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Web Socket handlers."""

import google.appengine.ext.webapp
import google.appengine.ext.webapp.template
import google.appengine.ext.webapp.util
import logging
import typhoonae.websocket
import urllib


class MainHandler(google.appengine.ext.webapp.RequestHandler):
    """Provides the file upload form."""

    def get(self):
        """Handles get."""

        websocket_url = typhoonae.websocket.create_websocket_url()

        output = google.appengine.ext.webapp.template.render(
            'websocket.html', {'websocket_url': websocket_url})
        self.response.out.write(output)


class WebSocketHandler(google.appengine.ext.webapp.RequestHandler):
    """Handles Web Socket requests."""

    def post(self):
        """Handles post."""

        message = typhoonae.websocket.Message(self.request.POST)
        typhoonae.websocket.send_message(
            [message.socket], 'Received: "%s"' % message.body)


app = google.appengine.ext.webapp.WSGIApplication([
    ('/websocket', MainHandler),
    ('/_ah/websocket/message/', WebSocketHandler),
], debug=True)


def main():
    """The main function."""

    google.appengine.ext.webapp.util.run_wsgi_app(app)


if __name__ == '__main__':
    main()
