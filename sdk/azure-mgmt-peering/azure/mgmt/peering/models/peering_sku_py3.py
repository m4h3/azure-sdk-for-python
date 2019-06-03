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


class PeeringSku(Model):
    """The SKU that defines the tier and kind of the peering.

    :param name: The name of the peering SKU. Possible values include:
     'Basic_Exchange_Free', 'Basic_Direct_Free', 'Premium_Direct_Free',
     'Premium_Exchange_Metered'
    :type name: str or ~azure.mgmt.peering.models.Name
    :param tier: The tier of the peering SKU. Possible values include:
     'Basic', 'Premium'
    :type tier: str or ~azure.mgmt.peering.models.Tier
    :param family: The family of the peering SKU. Possible values include:
     'Direct', 'Exchange'
    :type family: str or ~azure.mgmt.peering.models.Family
    :param size: The size of the peering SKU. Possible values include: 'Free',
     'Metered', 'Unlimited'
    :type size: str or ~azure.mgmt.peering.models.Size
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
    }

    def __init__(self, *, name=None, tier=None, family=None, size=None, **kwargs) -> None:
        super(PeeringSku, self).__init__(**kwargs)
        self.name = name
        self.tier = tier
        self.family = family
        self.size = size
