### Tracking Pittsburghs Busess Never Been so Easy.

The purpose of this application is to spin up and track bus locations across the entire Port Authority System.

## Pittsburgh Port Authority Requirements

You need to have an API key through: https://truetime.portauthority.org/bustime/home.jsp

This will allow you to ping the live data from Port Authority.

## History

We need a backstop for History.  We dont need to know ALL history indefinately, so to keep the Elasticsearch Database small, the backstop will be 1 Month.  This is defined in the Config file, so each user can choose to save more or less data.  1 Month is enough because you will generally see Routes of all buses and garage stops.  Using Kibana or ES to do ML to determine hiccups in routes will easily be determined with a month of history.  It will project traffic and hiccups with a month of routes and timelines.