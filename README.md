# gae-django
Python Django application deployed on Google App Engine


[![Build Status](https://travis-ci.org/egenerat/gae-django.svg?branch=master)](https://travis-ci.org/egenerat/gae-django)

Run server in debug mode
--automatic_restart=no --max_module_instances=default:1

Specific datastore
--datastore_path=/path/to/datastore

Push updates
appcfg.py update .

python2.7 dev_appserver.py --automatic_restart=no --max_module_instances=default:1 .