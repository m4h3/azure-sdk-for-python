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
    from .text_word_py3 import TextWord
    from .text_line_py3 import TextLine
    from .read_result_py3 import ReadResult
    from .key_value_element_py3 import KeyValueElement
    from .key_value_pair_py3 import KeyValuePair
    from .data_table_cell_py3 import DataTableCell
    from .data_table_py3 import DataTable
    from .page_result_py3 import PageResult
    from .field_value_py3 import FieldValue
    from .document_result_py3 import DocumentResult
    from .error_information_py3 import ErrorInformation
    from .analyze_result_py3 import AnalyzeResult
    from .analyze_operation_result_py3 import AnalyzeOperationResult
    from .train_source_filter_py3 import TrainSourceFilter
    from .train_request_py3 import TrainRequest
    from .training_document_info_py3 import TrainingDocumentInfo
    from .form_fields_report_py3 import FormFieldsReport
    from .train_result_py3 import TrainResult
    from .source_path_py3 import SourcePath
    from .model_info_py3 import ModelInfo
    from .models_summary_py3 import ModelsSummary
    from .models_model_py3 import ModelsModel
    from .keys_result_py3 import KeysResult
    from .model_py3 import Model
    from .error_response_py3 import ErrorResponse, ErrorResponseException
except (SyntaxError, ImportError):
    from .text_word import TextWord
    from .text_line import TextLine
    from .read_result import ReadResult
    from .key_value_element import KeyValueElement
    from .key_value_pair import KeyValuePair
    from .data_table_cell import DataTableCell
    from .data_table import DataTable
    from .page_result import PageResult
    from .field_value import FieldValue
    from .document_result import DocumentResult
    from .error_information import ErrorInformation
    from .analyze_result import AnalyzeResult
    from .analyze_operation_result import AnalyzeOperationResult
    from .train_source_filter import TrainSourceFilter
    from .train_request import TrainRequest
    from .training_document_info import TrainingDocumentInfo
    from .form_fields_report import FormFieldsReport
    from .train_result import TrainResult
    from .source_path import SourcePath
    from .model_info import ModelInfo
    from .models_summary import ModelsSummary
    from .models_model import ModelsModel
    from .keys_result import KeysResult
    from .model import Model
    from .error_response import ErrorResponse, ErrorResponseException
from .form_recognizer_client_enums import (
    OperationStatus,
    LengthUnit,
    Language,
    FieldValueType,
    TrainStatus,
    ModelStatus,
)

__all__ = [
    'TextWord',
    'TextLine',
    'ReadResult',
    'KeyValueElement',
    'KeyValuePair',
    'DataTableCell',
    'DataTable',
    'PageResult',
    'FieldValue',
    'DocumentResult',
    'ErrorInformation',
    'AnalyzeResult',
    'AnalyzeOperationResult',
    'TrainSourceFilter',
    'TrainRequest',
    'TrainingDocumentInfo',
    'FormFieldsReport',
    'TrainResult',
    'SourcePath',
    'ModelInfo',
    'ModelsSummary',
    'ModelsModel',
    'KeysResult',
    'Model',
    'ErrorResponse', 'ErrorResponseException',
    'OperationStatus',
    'LengthUnit',
    'Language',
    'FieldValueType',
    'TrainStatus',
    'ModelStatus',
]
