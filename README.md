# Flight-manager
Python Django application deployed on Google App Engine


[![Build Status](https://travis-ci.org/egenerat/flight-manager.svg?branch=master)](https://travis-ci.org/egenerat/gae-django)

Run server in debug mode
`--automatic_restart=no --max_module_instances=default:1`

Specific datastore
`--datastore_path=/path/to/datastore`

Push updates
`appcfg.py update .`

`python2.7 dev_appserver.py --automatic_restart=no --max_module_instances=default:1 .`

Download code from app engine
`appcfg.py -A [YOUR_APP_ID] -V [YOUR_APP_VERSION] download_app [OUTPUT_DIR]`

appcfg.py list_versions .

appcfg.py set_default_version .