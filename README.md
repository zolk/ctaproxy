# CTA Bus Tracker Proxy for Google App Engine

By Kevin Zolkiewicz

The Chicago Transit Authority's [Bus Tracker API](http://www.transitchicago.com/developers/bustracker.aspx) has a transaction limit of 10,000 transactions/day. Use of a proxy that caches requests can help your application remain under this limit. This is Phyton-based application designed for deployment on [Google App Engine](http://code.google.com/appengine/) that provides a proxy for Bus Tracker's getRoutes, getDirections, getStops, and getPredictions APIs. Requests to getRoutes, getDirections, and getStops are cached for a period of one day. Requests to getPredictions are cached for a period of 45 seconds.

This application is used by my [Bus Tracker Widget for Mac OS X](http://widget.chicagobus.org/).

If you see something in the code that can be done better, feel free to send a pull request.