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

try:
    from ._models_py3 import AKS
    from ._models_py3 import AksComputeSecrets
    from ._models_py3 import AksNetworkingConfiguration
    from ._models_py3 import AKSProperties
    from ._models_py3 import AmlCompute
    from ._models_py3 import AmlComputeNodeInformation
    from ._models_py3 import AmlComputeNodesInformation
    from ._models_py3 import AmlComputeProperties
    from ._models_py3 import AmlInstance
    from ._models_py3 import AmlInstanceApplicationUri
    from ._models_py3 import AmlInstanceConnectivityEndpoints
    from ._models_py3 import AmlInstanceCreatedBy
    from ._models_py3 import AmlInstanceCustomScriptSettings
    from ._models_py3 import AmlInstanceCustomScriptSettingsStartupScript
    from ._models_py3 import AmlInstanceDatastore
    from ._models_py3 import AmlInstanceDatastoresMountSettings
    from ._models_py3 import AmlInstanceOSUpdateSettings
    from ._models_py3 import AmlInstanceProperties
    from ._models_py3 import AmlInstanceSdkUpdate
    from ._models_py3 import AmlInstanceSdkUpdateSettings
    from ._models_py3 import AmlInstanceSoftwareUpdateSettings
    from ._models_py3 import AmlInstanceSshSettings
    from ._models_py3 import ClusterUpdateParameters
    from ._models_py3 import Compute
    from ._models_py3 import ComputeNodesInformation
    from ._models_py3 import ComputeResource
    from ._models_py3 import ComputeSecrets
    from ._models_py3 import Databricks
    from ._models_py3 import DatabricksComputeSecrets
    from ._models_py3 import DatabricksProperties
    from ._models_py3 import DataFactory
    from ._models_py3 import DataLakeAnalytics
    from ._models_py3 import DataLakeAnalyticsProperties
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import HDInsight
    from ._models_py3 import HDInsightProperties
    from ._models_py3 import Identity
    from ._models_py3 import ListWorkspaceKeysResult
    from ._models_py3 import MachineLearningServiceError, MachineLearningServiceErrorException
    from ._models_py3 import NodeStateCounts
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import Password
    from ._models_py3 import QuotaBaseProperties
    from ._models_py3 import QuotaUpdateParameters
    from ._models_py3 import RegistryListCredentialsResult
    from ._models_py3 import Resource
    from ._models_py3 import ResourceId
    from ._models_py3 import ResourceName
    from ._models_py3 import ResourceQuota
    from ._models_py3 import ScaleSettings
    from ._models_py3 import ServicePrincipalCredentials
    from ._models_py3 import SslConfiguration
    from ._models_py3 import SystemService
    from ._models_py3 import UpdateWorkspaceQuotas
    from ._models_py3 import UpdateWorkspaceQuotasResult
    from ._models_py3 import Usage
    from ._models_py3 import UsageName
    from ._models_py3 import UserAccountCredentials
    from ._models_py3 import VirtualMachine
    from ._models_py3 import VirtualMachineProperties
    from ._models_py3 import VirtualMachineSecrets
    from ._models_py3 import VirtualMachineSize
    from ._models_py3 import VirtualMachineSizeListResult
    from ._models_py3 import VirtualMachineSshCredentials
    from ._models_py3 import Workspace
    from ._models_py3 import WorkspaceUpdateParameters
except (SyntaxError, ImportError):
    from ._models import AKS
    from ._models import AksComputeSecrets
    from ._models import AksNetworkingConfiguration
    from ._models import AKSProperties
    from ._models import AmlCompute
    from ._models import AmlComputeNodeInformation
    from ._models import AmlComputeNodesInformation
    from ._models import AmlComputeProperties
    from ._models import AmlInstance
    from ._models import AmlInstanceApplicationUri
    from ._models import AmlInstanceConnectivityEndpoints
    from ._models import AmlInstanceCreatedBy
    from ._models import AmlInstanceCustomScriptSettings
    from ._models import AmlInstanceCustomScriptSettingsStartupScript
    from ._models import AmlInstanceDatastore
    from ._models import AmlInstanceDatastoresMountSettings
    from ._models import AmlInstanceOSUpdateSettings
    from ._models import AmlInstanceProperties
    from ._models import AmlInstanceSdkUpdate
    from ._models import AmlInstanceSdkUpdateSettings
    from ._models import AmlInstanceSoftwareUpdateSettings
    from ._models import AmlInstanceSshSettings
    from ._models import ClusterUpdateParameters
    from ._models import Compute
    from ._models import ComputeNodesInformation
    from ._models import ComputeResource
    from ._models import ComputeSecrets
    from ._models import Databricks
    from ._models import DatabricksComputeSecrets
    from ._models import DatabricksProperties
    from ._models import DataFactory
    from ._models import DataLakeAnalytics
    from ._models import DataLakeAnalyticsProperties
    from ._models import ErrorDetail
    from ._models import ErrorResponse
    from ._models import HDInsight
    from ._models import HDInsightProperties
    from ._models import Identity
    from ._models import ListWorkspaceKeysResult
    from ._models import MachineLearningServiceError, MachineLearningServiceErrorException
    from ._models import NodeStateCounts
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import Password
    from ._models import QuotaBaseProperties
    from ._models import QuotaUpdateParameters
    from ._models import RegistryListCredentialsResult
    from ._models import Resource
    from ._models import ResourceId
    from ._models import ResourceName
    from ._models import ResourceQuota
    from ._models import ScaleSettings
    from ._models import ServicePrincipalCredentials
    from ._models import SslConfiguration
    from ._models import SystemService
    from ._models import UpdateWorkspaceQuotas
    from ._models import UpdateWorkspaceQuotasResult
    from ._models import Usage
    from ._models import UsageName
    from ._models import UserAccountCredentials
    from ._models import VirtualMachine
    from ._models import VirtualMachineProperties
    from ._models import VirtualMachineSecrets
    from ._models import VirtualMachineSize
    from ._models import VirtualMachineSizeListResult
    from ._models import VirtualMachineSshCredentials
    from ._models import Workspace
    from ._models import WorkspaceUpdateParameters
from ._paged_models import ComputeResourcePaged
from ._paged_models import OperationPaged
from ._paged_models import ResourceQuotaPaged
from ._paged_models import UsagePaged
from ._paged_models import WorkspacePaged
from ._azure_machine_learning_workspaces_enums import (
    ProvisioningState,
    UsageUnit,
    QuotaUnit,
    Status,
    ResourceIdentityType,
    VmPriority,
    OsType,
    RemoteLoginPortPublicAccess,
    AllocationState,
    DatastoreSelection,
    DatastoreState,
    OsUpdateType,
    UpdateOnNextStart,
    SshPublicAccess,
    AmlInstanceState,
    NodeState,
    ComputeType,
    UnderlyingResourceAction,
)

__all__ = [
    'AKS',
    'AksComputeSecrets',
    'AksNetworkingConfiguration',
    'AKSProperties',
    'AmlCompute',
    'AmlComputeNodeInformation',
    'AmlComputeNodesInformation',
    'AmlComputeProperties',
    'AmlInstance',
    'AmlInstanceApplicationUri',
    'AmlInstanceConnectivityEndpoints',
    'AmlInstanceCreatedBy',
    'AmlInstanceCustomScriptSettings',
    'AmlInstanceCustomScriptSettingsStartupScript',
    'AmlInstanceDatastore',
    'AmlInstanceDatastoresMountSettings',
    'AmlInstanceOSUpdateSettings',
    'AmlInstanceProperties',
    'AmlInstanceSdkUpdate',
    'AmlInstanceSdkUpdateSettings',
    'AmlInstanceSoftwareUpdateSettings',
    'AmlInstanceSshSettings',
    'ClusterUpdateParameters',
    'Compute',
    'ComputeNodesInformation',
    'ComputeResource',
    'ComputeSecrets',
    'Databricks',
    'DatabricksComputeSecrets',
    'DatabricksProperties',
    'DataFactory',
    'DataLakeAnalytics',
    'DataLakeAnalyticsProperties',
    'ErrorDetail',
    'ErrorResponse',
    'HDInsight',
    'HDInsightProperties',
    'Identity',
    'ListWorkspaceKeysResult',
    'MachineLearningServiceError', 'MachineLearningServiceErrorException',
    'NodeStateCounts',
    'Operation',
    'OperationDisplay',
    'Password',
    'QuotaBaseProperties',
    'QuotaUpdateParameters',
    'RegistryListCredentialsResult',
    'Resource',
    'ResourceId',
    'ResourceName',
    'ResourceQuota',
    'ScaleSettings',
    'ServicePrincipalCredentials',
    'SslConfiguration',
    'SystemService',
    'UpdateWorkspaceQuotas',
    'UpdateWorkspaceQuotasResult',
    'Usage',
    'UsageName',
    'UserAccountCredentials',
    'VirtualMachine',
    'VirtualMachineProperties',
    'VirtualMachineSecrets',
    'VirtualMachineSize',
    'VirtualMachineSizeListResult',
    'VirtualMachineSshCredentials',
    'Workspace',
    'WorkspaceUpdateParameters',
    'OperationPaged',
    'WorkspacePaged',
    'UsagePaged',
    'ResourceQuotaPaged',
    'ComputeResourcePaged',
    'ProvisioningState',
    'UsageUnit',
    'QuotaUnit',
    'Status',
    'ResourceIdentityType',
    'VmPriority',
    'OsType',
    'RemoteLoginPortPublicAccess',
    'AllocationState',
    'DatastoreSelection',
    'DatastoreState',
    'OsUpdateType',
    'UpdateOnNextStart',
    'SshPublicAccess',
    'AmlInstanceState',
    'NodeState',
    'ComputeType',
    'UnderlyingResourceAction',
]
