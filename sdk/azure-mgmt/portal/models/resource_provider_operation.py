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


class ResourceProviderOperation(Model):
    """Supported operations of this resource provider.

    :param name: Operation name, in format of
     {provider}/{resource}/{operation}
    :type name: str
    :param is_data_action: Indicates whether the operation applies to
     data-plane.
    :type is_data_action: str
    :param display: Display metadata associated with the operation.
    :type display: ~microsoft.portal.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_data_action': {'key': 'isDataAction', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(self, **kwargs):
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_data_action = kwargs.get('is_data_action', None)
        self.display = kwargs.get('display', None)
