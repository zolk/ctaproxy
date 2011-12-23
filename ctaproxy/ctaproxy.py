import urllib
import time

from google.appengine.api import urlfetch
from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class getRoutes(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/xml'
    self.response.headers['Cache-Control'] = 'max-age=86400'

    key = self.request.get('key')
    url = 'http://ctabustracker.com/bustime/api/v1/getroutes?key=' + key + ''

    data = memcache.get(url)
    if data is not None:
        self.response.out.write(data)
    else:
        result = urlfetch.fetch(url)
        memcache.add(key=url, value=result.content, time=86400)
        self.response.out.write(result.content)

class getDirections(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/xml'
    self.response.headers['Cache-Control'] = 'max-age=86400'

    key = self.request.get('key')
    rt = self.request.get('rt')
    url = 'http://ctabustracker.com/bustime/api/v1/getdirections?key=' + key + '&rt=' + rt + ''

    data = memcache.get(url)
    if data is not None:
        self.response.out.write(data)
    else:
        result = urlfetch.fetch(url)
        memcache.add(key=url, value=result.content, time=86400)
        self.response.out.write(result.content)

class getStops(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/xml'
    self.response.headers['Cache-Control'] = 'max-age=86400'

    key = self.request.get('key')
    rt = self.request.get('rt')
    dir = urllib.quote(self.request.get('dir'))
    url = 'http://ctabustracker.com/bustime/api/v1/getstops?key=' + key + '&rt=' + rt + '&dir=' + dir + ''

    data = memcache.get(url)
    if data is not None:
        self.response.out.write(data)
    else:
        result = urlfetch.fetch(url)
        memcache.add(key=url, value=result.content, time=86400)
        self.response.out.write(result.content)

class getPredictions(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/xml'
    self.response.headers['Cache-Control'] = 'max-age=45'

    key = self.request.get('key')
    rt = self.request.get('rt')
    stpid = self.request.get('stpid')
    url = 'http://www.ctabustracker.com/bustime/api/v1/getpredictions?key=' + key + '&rt=' + rt + '&stpid=' + stpid + ''
    
    data = memcache.get(url)
    if data is not None:
        self.response.out.write(data)
    else:
        result = urlfetch.fetch(url)
        memcache.add(key=url, value=result.content, time=45)
        self.response.out.write(result.content)
        
application = webapp.WSGIApplication(
                                     [('/bustime/api/v1/getroutes', getRoutes),
                                      ('/bustime/api/v1/getdirections', getDirections),
                                      ('/bustime/api/v1/getstops', getStops),
                                      ('/bustime/api/v1/getpredictions', getPredictions)])

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()