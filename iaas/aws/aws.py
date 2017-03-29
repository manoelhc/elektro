#!/usr/bin/env python3

from iaas.iaas import iaas
import os
import jinja2
from subprocess import call


class aws(iaas):
    def __init__(self):
        pass

    def render(self, tpl_path, context):
        path, filename = os.path.split(tpl_path)
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
        ).get_template(filename).render(context)

    def apply(self, data):
        elektro_home = "{}/.elektro/{}".format(os.path.expanduser("~"), data['name'])
        tf = open("{}/{}.tf".format(elektro_home, data['name']),'w')
        tf.write(self.render('aws.tf.j2', data))
        tf.close()
        call(["terraform", "apply"], cwd=elektro_home)
