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


class ManagementGroup(Model):
    """The management group details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID for the management group.  For example,
     /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
    :vartype id: str
    :ivar type: The type of the resource.  For example,
     Microsoft.Management/managementGroups
    :vartype type: str
    :ivar name: The name of the management group. For example,
     00000000-0000-0000-0000-000000000000
    :vartype name: str
    :param tenant_id: The AAD Tenant ID associated with the management group.
     For example, 00000000-0000-0000-0000-000000000000
    :type tenant_id: str
    :param display_name: The friendly name of the management group.
    :type display_name: str
    :param roles: The role definitions associated with the management group.
    :type roles: list[str]
    :param details: Details.
    :type details: ~azure.mgmt.managementgroups.models.ManagementGroupDetails
    :param children: The list of children.
    :type children:
     list[~azure.mgmt.managementgroups.models.ManagementGroupChildInfo]
    :param path: The hierarchial path from the root group to the current
     group.
    :type path:
     list[~azure.mgmt.managementgroups.models.ManagementGroupPathElement]
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'roles': {'key': 'properties.roles', 'type': '[str]'},
        'details': {'key': 'properties.details', 'type': 'ManagementGroupDetails'},
        'children': {'key': 'properties.children', 'type': '[ManagementGroupChildInfo]'},
        'path': {'key': 'properties.path', 'type': '[ManagementGroupPathElement]'},
    }

    def __init__(self, *, tenant_id: str=None, display_name: str=None, roles=None, details=None, children=None, path=None, **kwargs) -> None:
        super(ManagementGroup, self).__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = None
        self.tenant_id = tenant_id
        self.display_name = display_name
        self.roles = roles
        self.details = details
        self.children = children
        self.path = path
