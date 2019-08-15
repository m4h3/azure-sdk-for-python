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


class BaseAlertRuleTemplateProperties(Model):
    """Base alert rule template property bag.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param display_name: The display name for alert rule template.
    :type display_name: str
    :param description: The description of the alert rule template.
    :type description: str
    :param tactics: The tactics of the alert rule template
    :type tactics: list[str or
     ~azure.mgmt.securityinsight.models.AttackTactic]
    :ivar created_date_utc: The time that this alert rule template has been
     added.
    :vartype created_date_utc: str
    :param status: The alert rule template status. Possible values include:
     'Installed', 'Available', 'NotAvailable'
    :type status: str or ~azure.mgmt.securityinsight.models.TemplateStatus
    :param required_data_connectors: The required data connectors for this
     template
    :type required_data_connectors:
     list[~azure.mgmt.securityinsight.models.DataConnectorStatus]
    :param alert_rules_created_by_template_count: the number of alert rules
     that were created by this template
    :type alert_rules_created_by_template_count: int
    """

    _validation = {
        'created_date_utc': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'tactics': {'key': 'tactics', 'type': '[AttackTactic]'},
        'created_date_utc': {'key': 'createdDateUTC', 'type': 'str'},
        'status': {'key': 'status', 'type': 'TemplateStatus'},
        'required_data_connectors': {'key': 'requiredDataConnectors', 'type': '[DataConnectorStatus]'},
        'alert_rules_created_by_template_count': {'key': 'alertRulesCreatedByTemplateCount', 'type': 'int'},
    }

    def __init__(self, *, display_name: str=None, description: str=None, tactics=None, status=None, required_data_connectors=None, alert_rules_created_by_template_count: int=None, **kwargs) -> None:
        super(BaseAlertRuleTemplateProperties, self).__init__(**kwargs)
        self.display_name = display_name
        self.description = description
        self.tactics = tactics
        self.created_date_utc = None
        self.status = status
        self.required_data_connectors = required_data_connectors
        self.alert_rules_created_by_template_count = alert_rules_created_by_template_count