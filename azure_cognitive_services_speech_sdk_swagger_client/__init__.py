# coding: utf-8

# flake8: noqa

"""
    Speech Services API v3.1

    Speech Services API v3.1.  # noqa: E501

    OpenAPI spec version: v3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from azure_cognitive_services_speech_sdk_swagger_client.api.default_api import (
    DefaultApi,
)

# import ApiClient
from azure_cognitive_services_speech_sdk_swagger_client.api_client import ApiClient
from azure_cognitive_services_speech_sdk_swagger_client.configuration import (
    Configuration,
)

# import models into sdk package
from azure_cognitive_services_speech_sdk_swagger_client.models.base_model import (
    BaseModel,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.base_model_deprecation_dates import (
    BaseModelDeprecationDates,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.base_model_features import (
    BaseModelFeatures,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.base_model_links import (
    BaseModelLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.base_model_properties import (
    BaseModelProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.block_kind import (
    BlockKind,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.body import Body
from azure_cognitive_services_speech_sdk_swagger_client.models.commit_blocks_entry import (
    CommitBlocksEntry,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.commit_blocks_entry_array import (
    CommitBlocksEntryArray,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.component import (
    Component,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.custom_model import (
    CustomModel,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.custom_model_deprecation_dates import (
    CustomModelDeprecationDates,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.custom_model_features import (
    CustomModelFeatures,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.custom_model_links import (
    CustomModelLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.custom_model_properties import (
    CustomModelProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.dataset import Dataset
from azure_cognitive_services_speech_sdk_swagger_client.models.dataset_kind import (
    DatasetKind,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.dataset_links import (
    DatasetLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.dataset_locales import (
    DatasetLocales,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.dataset_properties import (
    DatasetProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.dataset_update import (
    DatasetUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.detailed_error_code import (
    DetailedErrorCode,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.diarization_properties import (
    DiarizationProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.diarization_speakers_properties import (
    DiarizationSpeakersProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.endpoint import Endpoint
from azure_cognitive_services_speech_sdk_swagger_client.models.endpoint_links import (
    EndpointLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.endpoint_properties import (
    EndpointProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.endpoint_properties_update import (
    EndpointPropertiesUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.endpoint_update import (
    EndpointUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.endpoints_locales_get200_application_json_response import (
    EndpointsLocalesGet200ApplicationJsonResponse,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.entity_error import (
    EntityError,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.entity_reference import (
    EntityReference,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.error import Error
from azure_cognitive_services_speech_sdk_swagger_client.models.error_code import (
    ErrorCode,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.evaluation import (
    Evaluation,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.evaluation_links import (
    EvaluationLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.evaluation_properties import (
    EvaluationProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.evaluation_update import (
    EvaluationUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.evaluations_locales_get200_application_json_response import (
    EvaluationsLocalesGet200ApplicationJsonResponse,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.file import File
from azure_cognitive_services_speech_sdk_swagger_client.models.file_kind import FileKind
from azure_cognitive_services_speech_sdk_swagger_client.models.file_links import (
    FileLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.file_properties import (
    FileProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.health_status import (
    HealthStatus,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.inner_error import (
    InnerError,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.language_identification_properties import (
    LanguageIdentificationProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.model_copy import (
    ModelCopy,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.model_file import (
    ModelFile,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.model_manifest import (
    ModelManifest,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.model_update import (
    ModelUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.models_locales_get200_application_json_response import (
    ModelsLocalesGet200ApplicationJsonResponse,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_base_models import (
    PaginatedBaseModels,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_custom_models import (
    PaginatedCustomModels,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_datasets import (
    PaginatedDatasets,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_endpoints import (
    PaginatedEndpoints,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_evaluations import (
    PaginatedEvaluations,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_files import (
    PaginatedFiles,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_projects import (
    PaginatedProjects,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_transcriptions import (
    PaginatedTranscriptions,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.paginated_web_hooks import (
    PaginatedWebHooks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.profanity_filter_mode import (
    ProfanityFilterMode,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.project import Project
from azure_cognitive_services_speech_sdk_swagger_client.models.project_links import (
    ProjectLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.project_properties import (
    ProjectProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.project_update import (
    ProjectUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.projects_locales_get200_application_json_response import (
    ProjectsLocalesGet200ApplicationJsonResponse,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.punctuation_mode import (
    PunctuationMode,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.response_block import (
    ResponseBlock,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.service_health import (
    ServiceHealth,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.shared_model import (
    SharedModel,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.shared_model_features import (
    SharedModelFeatures,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.status import Status
from azure_cognitive_services_speech_sdk_swagger_client.models.transcription import (
    Transcription,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.transcription_links import (
    TranscriptionLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.transcription_properties import (
    TranscriptionProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.transcription_update import (
    TranscriptionUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.transcriptions_locales_get200_application_json_response import (
    TranscriptionsLocalesGet200ApplicationJsonResponse,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.uploaded_blocks import (
    UploadedBlocks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.web_hook import WebHook
from azure_cognitive_services_speech_sdk_swagger_client.models.web_hook_events import (
    WebHookEvents,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.web_hook_links import (
    WebHookLinks,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.web_hook_properties import (
    WebHookProperties,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.web_hook_properties_update import (
    WebHookPropertiesUpdate,
)
from azure_cognitive_services_speech_sdk_swagger_client.models.web_hook_update import (
    WebHookUpdate,
)
