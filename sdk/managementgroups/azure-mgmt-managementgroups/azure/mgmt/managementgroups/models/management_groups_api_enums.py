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

from enum import Enum


class Reason(str, Enum):

    invalid = "Invalid"
    already_exists = "AlreadyExists"


class Status(str, Enum):

    not_started = "NotStarted"
    not_started_but_groups_exist = "NotStartedButGroupsExist"
    started = "Started"
    failed = "Failed"
    cancelled = "Cancelled"
    completed = "Completed"


class Type(str, Enum):

    microsoft_managementmanagement_groups = "Microsoft.Management/managementGroups"
