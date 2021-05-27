#from pybuilder.core import task
#
#@task
#def say_hello (logger):
#   logger.info("Hello, PyBuilder")
#    
#from pybuilder.core import use_plugin
#
#use_plugin("python.core")
#
#default_task = "publish"

from pybuilder.core import use_plugin, init

# These are the plugins we want to use in our project.
# Projects provide tasks which are blocks of logic executed by PyBuilder.

use_plugin("python.core")
# the python unittest plugin allows running python's standard library unittests
use_plugin("python.unittest")
# this plugin allows installing project dependencies with pip
use_plugin("python.install_dependencies")
# a linter plugin that runs flake8 (pyflakes + pep8) on our project sources
use_plugin("python.flake8")
# a plugin that measures unit test statement coverage
use_plugin("python.coverage")
# for packaging purposes since we'll build a tarball
use_plugin("python.distutils")


# The project name
name = "myproject"
# What PyBuilder should run when no tasks are given.
# Calling "pyb" amounts to calling "pyb publish" here.
# We could run several tasks by assigning a list to `default_task`.
default_task = "publish"


# This is an initializer, a block of logic that runs before the project is built.
@init
def set_properties(project):
    # Nothing happens here yet, but notice the `project` argument which is automatically injected.
    pass