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
        vf = open('{}/variables.tf'.format(elektro_home),'w')
        tf = open('{}/{}.tf'.format(elektro_home, data['name']),'w')
        tf.write(self.render('aws.tf.j2', data))
        tf.close()
        vf.write('variable "aws_access_key" {} default = "{}" {}'.format('{',os.getenv('AWS_ACCESS_KEY_ID'),'}'))
        vf.write("\n")
        vf.write('variable "aws_secret_key" {} default = "{}" {}'.format('{',os.getenv('AWS_SECRET_ACCESS_KEY'),'}'))
        vf.write("\n")
        vf.close()
        call(["terraform", "apply"], cwd=elektro_home)
