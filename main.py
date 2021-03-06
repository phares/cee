#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import jinja2
import os


template_path = os.path.join(os.path.dirname(__file__))

jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_path))

template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/index.html')
        self.response.out.write(template.render(template_values))

class ServicesHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/service.html')
        self.response.out.write(template.render(template_values))

class BlogHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/blog.html')
        self.response.out.write(template.render(template_values))


class BlogDetailsHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/blog-details.html')
        self.response.out.write(template.render(template_values))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/contact.html')
        self.response.out.write(template.render(template_values))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {

        }
        notification = self.request.get('notification')
        if notification:
            template_values['notification'] = notification
        self.response.set_status(200)
        template = jinja2_env.get_template('templates/about.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/contact', ContactHandler),
    ('/services', ServicesHandler),
    ('/about', AboutHandler),
    ('/blog', BlogHandler),
    ('/blog-details', BlogDetailsHandler)
], debug=True)
