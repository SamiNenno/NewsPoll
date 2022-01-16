#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "NewsPoll"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python", "/Users/macbook/Desktop/Python_Files")
    project.set_property("dir_source_unittest_python", "Unittest_Scripts")
    project.depends_on_requirements("requirements.txt")
