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


class ModelProperties(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'deprecation_dates': 'ModelDeprecationDates',
        'email': 'str',
        'error': 'EntityError'
    }

    attribute_map = {
        'deprecation_dates': 'deprecationDates',
        'email': 'email',
        'error': 'error'
    }

    def __init__(self, deprecation_dates=None, email=None, error=None, _configuration=None):  # noqa: E501
        """ModelProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deprecation_dates = None
        self._email = None
        self._error = None
        self.discriminator = None

        if deprecation_dates is not None:
            self.deprecation_dates = deprecation_dates
        if email is not None:
            self.email = email
        if error is not None:
            self.error = error

    @property
    def deprecation_dates(self):
        """Gets the deprecation_dates of this ModelProperties.  # noqa: E501


        :return: The deprecation_dates of this ModelProperties.  # noqa: E501
        :rtype: ModelDeprecationDates
        """
        return self._deprecation_dates

    @deprecation_dates.setter
    def deprecation_dates(self, deprecation_dates):
        """Sets the deprecation_dates of this ModelProperties.


        :param deprecation_dates: The deprecation_dates of this ModelProperties.  # noqa: E501
        :type: ModelDeprecationDates
        """

        self._deprecation_dates = deprecation_dates

    @property
    def email(self):
        """Gets the email of this ModelProperties.  # noqa: E501

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :return: The email of this ModelProperties.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelProperties.

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :param email: The email of this ModelProperties.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error(self):
        """Gets the error of this ModelProperties.  # noqa: E501


        :return: The error of this ModelProperties.  # noqa: E501
        :rtype: EntityError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ModelProperties.


        :param error: The error of this ModelProperties.  # noqa: E501
        :type: EntityError
        """

        self._error = error

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
        if issubclass(ModelProperties, dict):
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
        if not isinstance(other, ModelProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelProperties):
            return True

        return self.to_dict() != other.to_dict()