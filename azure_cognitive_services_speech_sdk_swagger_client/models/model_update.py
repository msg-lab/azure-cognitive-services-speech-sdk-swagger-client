# coding: utf-8

"""
    Speech Services API v3.1

    Speech Services API v3.1.  # noqa: E501

    OpenAPI spec version: v3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from azure_cognitive_services_speech_sdk_swagger_client.configuration import (
    Configuration,
)


class ModelUpdate(object):
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
        "project": "EntityReference",
        "display_name": "str",
        "description": "str",
        "custom_properties": "dict(str, str)",
    }

    attribute_map = {
        "project": "project",
        "display_name": "displayName",
        "description": "description",
        "custom_properties": "customProperties",
    }

    def __init__(
        self,
        project=None,
        display_name=None,
        description=None,
        custom_properties=None,
        _configuration=None,
    ):  # noqa: E501
        """ModelUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._project = None
        self._display_name = None
        self._description = None
        self._custom_properties = None
        self.discriminator = None

        if project is not None:
            self.project = project
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if custom_properties is not None:
            self.custom_properties = custom_properties

    @property
    def project(self):
        """Gets the project of this ModelUpdate.  # noqa: E501


        :return: The project of this ModelUpdate.  # noqa: E501
        :rtype: EntityReference
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ModelUpdate.


        :param project: The project of this ModelUpdate.  # noqa: E501
        :type: EntityReference
        """

        self._project = project

    @property
    def display_name(self):
        """Gets the display_name of this ModelUpdate.  # noqa: E501

        The name of the object.  # noqa: E501

        :return: The display_name of this ModelUpdate.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ModelUpdate.

        The name of the object.  # noqa: E501

        :param display_name: The display_name of this ModelUpdate.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ModelUpdate.  # noqa: E501

        The description of the object.  # noqa: E501

        :return: The description of this ModelUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelUpdate.

        The description of the object.  # noqa: E501

        :param description: The description of this ModelUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def custom_properties(self):
        """Gets the custom_properties of this ModelUpdate.  # noqa: E501

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :return: The custom_properties of this ModelUpdate.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this ModelUpdate.

        The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10.  # noqa: E501

        :param custom_properties: The custom_properties of this ModelUpdate.  # noqa: E501
        :type: dict(str, str)
        """

        self._custom_properties = custom_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ModelUpdate, dict):
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
        if not isinstance(other, ModelUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelUpdate):
            return True

        return self.to_dict() != other.to_dict()
