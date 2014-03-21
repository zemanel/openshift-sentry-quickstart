Sentry on OpenShift
===================

A http://github.com/dcramer/sentry quickstart project for Red Hat(c) OpenShift(c).

-[![Build Status](https://travis-ci.org/zemanel/openshift-sentry-quickstart.png)](https://travis-ci.org/zemanel/openshift-sentry-quickstart)

Requirements
------------

- An Openshift account, with at least 3 gears available on the free PaaS https://openshift.redhat.com
- Openshift command-line tools: https://www.openshift.com/get-started#cli
- Git SCM: http://git-scm.com

Features
--------

- Python 2.7 scalable Openshift cartridge
- Django *staticfiles* support
- Django Database caching
- Django security unique secret key based on created instance

Deploying to Openshift
----------------------

**Create some local environment variables for being DRY**

Replace **MyOpenshiftNamespace** with your chosen namespace. You can edit your namespace at https://openshift.redhat.com/app/account/domain/edit

Replace **APP_NAME**'s value with your chosen app name. I've chosen **sentryweb** for this example.

    $ export QUICKSTART_URL=git@github.com:joaoxsouls/openshift-sentry-quickstart.git
    $ export APP_NAME=sentryweb
    $ export APP_NAMESPACE=MyOpenshiftNamespace

**Create Openshift application with Python 2.7, MongoDB 2.2, Postgres 8.4 cartridges, enabling scaling**

    $ rhc app create --scaling $APP_NAME python-2.7 mongodb-postgresql-8.4

**Merge the quickstart repo with the git repo created by the Openshift client**

    $ cd $APP_NAME
    $ git remote add upstream -m master $QUICKSTART_URL
    $ git pull -s recursive -X theirs upstream master
    $ git push origin

The project will be deployed to the remote application instance and if everything
works as intended, you will be able to access your Sentry instance at:

    https://APP_NAME-APP_NAMESPACE.rhcloud.com

Managing your Sentry application
--------------------------------

**Executing management commands**

Django management commands, as creating superusers, can be ran by using SSH:

    # SSH into the application
    $ rhc app ssh $APP_NAME

    # Activate the virtualenv
    $ source ${OPENSHIFT_HOMEDIR}python/virtenv/bin/activate

    # List available Django commands
    $ sentry --config=${OPENSHIFT_REPO_DIR}/sentry.conf.py help

**Creating a new user**

Since new account registration is disabled by default on the Sentry Openshift setttings, a Django user account can be created by using the **createsuperuser** command :

    $ sentry --config=${OPENSHIFT_REPO_DIR}/sentry.conf.py createsuperuser

You can now login with the account your created at

    https://APP_NAME-APP_NAMESPACE.rhcloud.com

and configure your new Sentry !

Django administration is also available at

    https://APP_NAME-APP_NAMESPACE.rhcloud.com/admin/

Further Reading
---------------

* http://github.com/dcramer/sentry
* http://sentry.readthedocs.org

Contributing
------------

Please send pull requests to the **develop** branch.

Supporting
----------

Feel free to https://www.gittip.com/zemanel/ me <3
