# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CheckNameAvailabilityRequest(Model):
    """Management group name availability check parameters.

    :param name: the name to check for availability
    :type name: str
    :param type: fully qualified resource type which includes provider
     namespace. Possible values include:
     'Microsoft.Management/managementGroups'
    :type type: str or ~azure.mgmt.managementgroups.models.Type
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'Type'},
    }

    def __init__(self, *, name: str=None, type=None, **kwargs) -> None:
        super(CheckNameAvailabilityRequest, self).__init__(**kwargs)
        self.name = name
        self.type = type
