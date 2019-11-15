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


class AnalyzeResult(Model):
    """Analyze operation result.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. Version of schema used for this result.
    :type version: str
    :param read_results: Required. Text extracted from the input.
    :type read_results:
     list[~azure.cognitiveservices.formrecognizer.models.ReadResult]
    :param page_results: Page-level information extracted from the input.
    :type page_results:
     list[~azure.cognitiveservices.formrecognizer.models.PageResult]
    :param document_results: Document-level information extracted from the
     input.
    :type document_results:
     list[~azure.cognitiveservices.formrecognizer.models.DocumentResult]
    :param errors: List of errors reported during the analyze operation.
    :type errors:
     list[~azure.cognitiveservices.formrecognizer.models.ErrorInformation]
    """

    _validation = {
        'version': {'required': True},
        'read_results': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'read_results': {'key': 'readResults', 'type': '[ReadResult]'},
        'page_results': {'key': 'pageResults', 'type': '[PageResult]'},
        'document_results': {'key': 'documentResults', 'type': '[DocumentResult]'},
        'errors': {'key': 'errors', 'type': '[ErrorInformation]'},
    }

    def __init__(self, *, version: str, read_results, page_results=None, document_results=None, errors=None, **kwargs) -> None:
        super(AnalyzeResult, self).__init__(**kwargs)
        self.version = version
        self.read_results = read_results
        self.page_results = page_results
        self.document_results = document_results
        self.errors = errors
