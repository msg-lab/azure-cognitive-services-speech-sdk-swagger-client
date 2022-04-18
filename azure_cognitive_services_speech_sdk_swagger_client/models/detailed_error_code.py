# coding: utf-8

"""
    Speech Services API v3.0

    Speech Services API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from azure_cognitive_services_speech_sdk_swagger_client.configuration import Configuration


class DetailedErrorCode(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    INVALIDPARAMETERVALUE = "InvalidParameterValue"
    INVALIDREQUESTBODYFORMAT = "InvalidRequestBodyFormat"
    EMPTYREQUEST = "EmptyRequest"
    MISSINGINPUTRECORDS = "MissingInputRecords"
    INVALIDDOCUMENT = "InvalidDocument"
    MODELVERSIONINCORRECT = "ModelVersionIncorrect"
    INVALIDDOCUMENTBATCH = "InvalidDocumentBatch"
    UNSUPPORTEDLANGUAGECODE = "UnsupportedLanguageCode"
    DATAIMPORTFAILED = "DataImportFailed"
    INUSEVIOLATION = "InUseViolation"
    INVALIDLOCALE = "InvalidLocale"
    INVALIDBASEMODEL = "InvalidBaseModel"
    INVALIDADAPTATIONMAPPING = "InvalidAdaptationMapping"
    INVALIDDATASET = "InvalidDataset"
    INVALIDTEST = "InvalidTest"
    FAILEDDATASET = "FailedDataset"
    INVALIDMODEL = "InvalidModel"
    INVALIDTRANSCRIPTION = "InvalidTranscription"
    INVALIDPAYLOAD = "InvalidPayload"
    INVALIDPARAMETER = "InvalidParameter"
    ENDPOINTWITHOUTLOGGING = "EndpointWithoutLogging"
    INVALIDPERMISSIONS = "InvalidPermissions"
    INVALIDPREREQUISITE = "InvalidPrerequisite"
    INVALIDPRODUCTID = "InvalidProductId"
    INVALIDSUBSCRIPTION = "InvalidSubscription"
    INVALIDPROJECT = "InvalidProject"
    INVALIDPROJECTKIND = "InvalidProjectKind"
    INVALIDRECORDINGSURI = "InvalidRecordingsUri"
    ONLYONEOFURLSORCONTAINERORDATASET = "OnlyOneOfUrlsOrContainerOrDataset"
    EXCEEDEDNUMBEROFRECORDINGSURIS = "ExceededNumberOfRecordingsUris"
    MODELMISMATCH = "ModelMismatch"
    PROJECTGENDERMISMATCH = "ProjectGenderMismatch"
    MODELDEPRECATED = "ModelDeprecated"
    MODELEXISTS = "ModelExists"
    MODELNOTDEPLOYABLE = "ModelNotDeployable"
    ENDPOINTNOTUPDATABLE = "EndpointNotUpdatable"
    SINGLEDEFAULTENDPOINT = "SingleDefaultEndpoint"
    ENDPOINTCANNOTBEDEFAULT = "EndpointCannotBeDefault"
    INVALIDMODELURI = "InvalidModelUri"
    SUBSCRIPTIONNOTFOUND = "SubscriptionNotFound"
    QUOTAVIOLATION = "QuotaViolation"
    UNSUPPORTEDDELTA = "UnsupportedDelta"
    UNSUPPORTEDFILTER = "UnsupportedFilter"
    UNSUPPORTEDPAGINATION = "UnsupportedPagination"
    UNSUPPORTEDDYNAMICCONFIGURATION = "UnsupportedDynamicConfiguration"
    UNSUPPORTEDORDERBY = "UnsupportedOrderBy"
    NOUTF8WITHBOM = "NoUtf8WithBom"
    MODELDEPLOYMENTNOTCOMPLETESTATE = "ModelDeploymentNotCompleteState"
    SKULIMITSEXIST = "SkuLimitsExist"
    DEPLOYINGFAILEDMODEL = "DeployingFailedModel"
    UNSUPPORTEDTIMERANGE = "UnsupportedTimeRange"
    INVALIDLOGDATE = "InvalidLogDate"
    INVALIDLOGID = "InvalidLogId"
    INVALIDLOGSTARTTIME = "InvalidLogStartTime"
    INVALIDLOGENDTIME = "InvalidLogEndTime"
    INVALIDTOPFORLOGS = "InvalidTopForLogs"
    INVALIDSKIPTOKENFORLOGS = "InvalidSkipTokenForLogs"
    DELETENOTALLOWED = "DeleteNotAllowed"
    FORBIDDEN = "Forbidden"
    DEPLOYNOTALLOWED = "DeployNotAllowed"
    UNEXPECTEDERROR = "UnexpectedError"
    INVALIDCOLLECTION = "InvalidCollection"
    INVALIDCALLBACKURI = "InvalidCallbackUri"
    INVALIDSASVALIDITYDURATION = "InvalidSasValidityDuration"
    INACCESSIBLECUSTOMERSTORAGE = "InaccessibleCustomerStorage"
    UNSUPPORTEDCLASSBASEDADAPTATION = "UnsupportedClassBasedAdaptation"
    INVALIDWEBHOOKEVENTKIND = "InvalidWebHookEventKind"
    INVALIDTIMETOLIVE = "InvalidTimeToLive"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, _configuration=None):  # noqa: E501
        """DetailedErrorCode - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DetailedErrorCode, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DetailedErrorCode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailedErrorCode):
            return True

        return self.to_dict() != other.to_dict()
