#!/usr/bin/env python3
import argparse
import sys
import os
from es import ES

def help():
    from subprocess import call
    call(["cat", "help"])

parser = argparse.ArgumentParser(description='Elektro deploys your Elastic Stack',
                                 prog='elektro')

parser.add_argument('command',
                  metavar='N',
                  type=str,
                  nargs=1,
                  help='command')
parser.add_argument("-n", "--name",
                  dest="cluster_name",
                  type=str,
                  help="VPC Network")

parser.add_argument("-z", "--zone",
                  dest="zone_name",
                  type=str,
                  help="Availability Zone")

parser.add_argument("-a", "--vpc-cidr",
                  dest="vpc_cidr",
                  type=str,
                  help="VPC's CIDR")
parser.add_argument("-e", "--elastic-instance-type",
                  default="t2.micro",
                  type=str,
                  dest="elastic_itype",
                  help="Instance type for Elasticesearch server")
parser.add_argument("-l", "--logstash-instance-type",
                  default="t2.micro",
                  type=str,
                  dest="logstash_itype",
                  help="Instance type for Logstash server")
parser.add_argument("-k", "--kibana-instance-type",
                  default="t2.micro",
                  type=str,
                  dest="kibana_itype",
                  help="Instance type for Kibana server")
parser.add_argument("-o", "--allow",
                  dest="allow_address",
                  type=str,
                  help="The machine that is allowed to use ElasticSearch")
parser.add_argument("-c", "--iaas",
                  default="aws",
                  type=str,
                  dest="iaas",
                  help="The machine that is allowed to use ElasticSearch")

args = parser.parse_args()
command = args.command[0].lower()
valid_commands = ['create']
planned_commands = ['delete', 'update', 'list', 'import', 'export']
if command in planned_commands:
    print("------------------------------------")
    print("THIS COMMAND IS NOT IMPLEMENTED YET!")
    print("------------------------------------")
if command not in valid_commands:
    help()
    sys.exit(1)

elektro_home = "{}/.elektro/{}".format(os.path.expanduser("~"), args.cluster_name)
if not os.path.exists(elektro_home):
    os.mkdir(elektro_home)

ecluster = ES(args.cluster_name, args.iaas)
ecluster.set_vpc_netaddr(args.vpc_cidr) \
        .set_command(command) \
        .set_zone(args.zone_name) \
        .set_logstash_itype(args.logstash_itype) \
        .set_elastic_itype(args.elastic_itype) \
        .set_kibana_itype(args.kibana_itype)

for addr in args.allow_address.split(','):
    ecluster.add_allowed_machine(addr)

ecluster.apply_changes()
