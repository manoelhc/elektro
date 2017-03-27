#!/usr/bin/env python3

from iaas.iaas import iaas

class aws(iaas):
    def __init__(self):
        pass
    def apply(self, data):
        elektro_home = "{}/.elektro".format(os.path.expanduser("~"))
        self._file = open("{}/{}.tf".format(elektro_home, data['name'], 'w')

        # Create VPC
        self._file.write('variable "vpc_id" {}')
        self._file.write('data "aws_vpc" "selected" {')
        self._file.write('id = "${var.vpc_id}"')
        self._file.write('}')
        self._file.write('resource "aws_subnet" "example" {')
        self._file.write('vpc_id            = "${data.aws_vpc.selected.id}"')
        self._file.write('availability_zone = "us-west-2a"')
        self._file.write('cidr_block        = "${cidrsubnet(data.aws_vpc.selected.cidr_block, 4, 1)}"')
        self._file.write('}')
