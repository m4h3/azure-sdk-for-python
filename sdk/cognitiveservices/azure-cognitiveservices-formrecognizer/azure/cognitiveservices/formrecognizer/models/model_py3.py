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


class Model(Model):
    """Response to the get custom model operation.

    All required parameters must be populated in order to send to Azure.

    :param model_info: Required.
    :type model_info: ~azure.cognitiveservices.formrecognizer.models.ModelInfo
    :param keys:
    :type keys: ~azure.cognitiveservices.formrecognizer.models.KeysResult
    :param train_result:
    :type train_result:
     ~azure.cognitiveservices.formrecognizer.models.TrainResult
    """

    _validation = {
        'model_info': {'required': True},
    }

    _attribute_map = {
        'model_info': {'key': 'modelInfo', 'type': 'ModelInfo'},
        'keys': {'key': 'keys', 'type': 'KeysResult'},
        'train_result': {'key': 'trainResult', 'type': 'TrainResult'},
    }

    def __init__(self, *, model_info, keys=None, train_result=None, **kwargs) -> None:
        super(Model, self).__init__(**kwargs)
        self.model_info = model_info
        self.keys = keys
        self.train_result = train_result
