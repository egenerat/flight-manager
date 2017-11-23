# Flight-manager
Python Django application deployed on Google App Engine


[![Build Status](https://travis-ci.org/egenerat/flight-manager.svg?branch=master)](https://travis-ci.org/egenerat/flight-manager)

Run server in debug mode
`--automatic_restart=no --max_module_instances=default:1`

Run one test
`python -m unittest app.test.airport.test_airport_parser`

Specific datastore
`--datastore_path=/path/to/datastore`

Push updates
`appcfg.py update .`

`python2.7 dev_appserver.py --automatic_restart=no --max_module_instances=default:1 .`

Download code from app engine
`appcfg.py -A [YOUR_APP_ID] -V [YOUR_APP_VERSION] download_app [OUTPUT_DIR]`

List versions
`appcfg.py list_versions .`

Set version
`appcfg.py set_default_version .`



Environment variable
`--env_var SKIP_MISSION_REFRESH=True`

Check if runs locally
`os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')`

Useful links:
- [Using the Local Development Server](https://cloud.google.com/appengine/docs/standard/python/tools/using-local-server)