#!/usr/bin/env python3
import os
from iaas.aws.aws import aws

class ES:
    def __init__(self, name, iaas):
        self._data = {}
        self._data['name'] = name
        self._data['allowed'] = []
        self._data['iaas_inst'] = None
        self.set_iaas(iaas)

    def get_elastic_itype(self):
        return self._data['elastic_itype']
    def set_elastic_itype(self, itype):
        self._data['elastic_itype'] = itype
        return self

    def get_kibana_itype(self):
        return self._data['kibana_itype']
    def set_kibana_itype(self, itype):
        self._data['kibana_itype'] = itype
        return self

    def get_logstash_itype(self):
        return self._data['logstash_itype']
    def set_logstash_itype(self, itype):
        self._data['logstash_itype'] = itype
        return self

    def get_vpc_netaddr(self):
        return self._data['vpc_cidr']
    def set_vpc_netaddr(self, netaddr):
        self._data['vpc_cidr'] = netaddr
        return self

    def get_iaas(self):
        return self._data['iaas']
    def set_iaas(self, iaas_name):
        self._data['iaas'] = iaas_name
        self._iaas_inst = aws()
        return self
    def get_iaas_instance(self):
        return self._iaas_inst

    def apply_changes(self):
        self._iaas_inst.apply(self._data)

    def get_allowed_machines(self):
        return self._data['allowed']

    def add_allowed_machine(self, ipaddr):
        self._data['allowed'].append(ipaddr)
        return self
    def del_allowed_machine(self, ipaddr):
        idx = self._data['allowed'].index(ipaddr)
        del self._data['allowed'][idx]
        return self

    def set_zone(self, zone):
        self._data['zone'] = zone
        return self
    def get_zone(self, ipaddr):
        return self._data['zone']

    def set_command(self, command):
        self._data['command'] = command
        return self
