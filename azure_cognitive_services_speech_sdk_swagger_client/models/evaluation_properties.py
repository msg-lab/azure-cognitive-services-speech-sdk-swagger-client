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


class EvaluationProperties(object):
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
        "word_error_rate2": "float",
        "word_error_rate1": "float",
        "sentence_error_rate2": "float",
        "sentence_count2": "int",
        "word_count2": "int",
        "correct_word_count2": "int",
        "word_substitution_count2": "int",
        "word_deletion_count2": "int",
        "word_insertion_count2": "int",
        "sentence_error_rate1": "float",
        "sentence_count1": "int",
        "word_count1": "int",
        "correct_word_count1": "int",
        "word_substitution_count1": "int",
        "word_deletion_count1": "int",
        "word_insertion_count1": "int",
        "email": "str",
        "error": "EntityError",
    }

    attribute_map = {
        "word_error_rate2": "wordErrorRate2",
        "word_error_rate1": "wordErrorRate1",
        "sentence_error_rate2": "sentenceErrorRate2",
        "sentence_count2": "sentenceCount2",
        "word_count2": "wordCount2",
        "correct_word_count2": "correctWordCount2",
        "word_substitution_count2": "wordSubstitutionCount2",
        "word_deletion_count2": "wordDeletionCount2",
        "word_insertion_count2": "wordInsertionCount2",
        "sentence_error_rate1": "sentenceErrorRate1",
        "sentence_count1": "sentenceCount1",
        "word_count1": "wordCount1",
        "correct_word_count1": "correctWordCount1",
        "word_substitution_count1": "wordSubstitutionCount1",
        "word_deletion_count1": "wordDeletionCount1",
        "word_insertion_count1": "wordInsertionCount1",
        "email": "email",
        "error": "error",
    }

    def __init__(
        self,
        word_error_rate2=None,
        word_error_rate1=None,
        sentence_error_rate2=None,
        sentence_count2=None,
        word_count2=None,
        correct_word_count2=None,
        word_substitution_count2=None,
        word_deletion_count2=None,
        word_insertion_count2=None,
        sentence_error_rate1=None,
        sentence_count1=None,
        word_count1=None,
        correct_word_count1=None,
        word_substitution_count1=None,
        word_deletion_count1=None,
        word_insertion_count1=None,
        email=None,
        error=None,
        _configuration=None,
    ):  # noqa: E501
        """EvaluationProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._word_error_rate2 = None
        self._word_error_rate1 = None
        self._sentence_error_rate2 = None
        self._sentence_count2 = None
        self._word_count2 = None
        self._correct_word_count2 = None
        self._word_substitution_count2 = None
        self._word_deletion_count2 = None
        self._word_insertion_count2 = None
        self._sentence_error_rate1 = None
        self._sentence_count1 = None
        self._word_count1 = None
        self._correct_word_count1 = None
        self._word_substitution_count1 = None
        self._word_deletion_count1 = None
        self._word_insertion_count1 = None
        self._email = None
        self._error = None
        self.discriminator = None

        if word_error_rate2 is not None:
            self.word_error_rate2 = word_error_rate2
        if word_error_rate1 is not None:
            self.word_error_rate1 = word_error_rate1
        if sentence_error_rate2 is not None:
            self.sentence_error_rate2 = sentence_error_rate2
        if sentence_count2 is not None:
            self.sentence_count2 = sentence_count2
        if word_count2 is not None:
            self.word_count2 = word_count2
        if correct_word_count2 is not None:
            self.correct_word_count2 = correct_word_count2
        if word_substitution_count2 is not None:
            self.word_substitution_count2 = word_substitution_count2
        if word_deletion_count2 is not None:
            self.word_deletion_count2 = word_deletion_count2
        if word_insertion_count2 is not None:
            self.word_insertion_count2 = word_insertion_count2
        if sentence_error_rate1 is not None:
            self.sentence_error_rate1 = sentence_error_rate1
        if sentence_count1 is not None:
            self.sentence_count1 = sentence_count1
        if word_count1 is not None:
            self.word_count1 = word_count1
        if correct_word_count1 is not None:
            self.correct_word_count1 = correct_word_count1
        if word_substitution_count1 is not None:
            self.word_substitution_count1 = word_substitution_count1
        if word_deletion_count1 is not None:
            self.word_deletion_count1 = word_deletion_count1
        if word_insertion_count1 is not None:
            self.word_insertion_count1 = word_insertion_count1
        if email is not None:
            self.email = email
        if error is not None:
            self.error = error

    @property
    def word_error_rate2(self):
        """Gets the word_error_rate2 of this EvaluationProperties.  # noqa: E501

        The word error rate of recognition with model2.  # noqa: E501

        :return: The word_error_rate2 of this EvaluationProperties.  # noqa: E501
        :rtype: float
        """
        return self._word_error_rate2

    @word_error_rate2.setter
    def word_error_rate2(self, word_error_rate2):
        """Sets the word_error_rate2 of this EvaluationProperties.

        The word error rate of recognition with model2.  # noqa: E501

        :param word_error_rate2: The word_error_rate2 of this EvaluationProperties.  # noqa: E501
        :type: float
        """

        self._word_error_rate2 = word_error_rate2

    @property
    def word_error_rate1(self):
        """Gets the word_error_rate1 of this EvaluationProperties.  # noqa: E501

        The word error rate of recognition with model1.  # noqa: E501

        :return: The word_error_rate1 of this EvaluationProperties.  # noqa: E501
        :rtype: float
        """
        return self._word_error_rate1

    @word_error_rate1.setter
    def word_error_rate1(self, word_error_rate1):
        """Sets the word_error_rate1 of this EvaluationProperties.

        The word error rate of recognition with model1.  # noqa: E501

        :param word_error_rate1: The word_error_rate1 of this EvaluationProperties.  # noqa: E501
        :type: float
        """

        self._word_error_rate1 = word_error_rate1

    @property
    def sentence_error_rate2(self):
        """Gets the sentence_error_rate2 of this EvaluationProperties.  # noqa: E501

        The sentence error rate of recognition with model2.  # noqa: E501

        :return: The sentence_error_rate2 of this EvaluationProperties.  # noqa: E501
        :rtype: float
        """
        return self._sentence_error_rate2

    @sentence_error_rate2.setter
    def sentence_error_rate2(self, sentence_error_rate2):
        """Sets the sentence_error_rate2 of this EvaluationProperties.

        The sentence error rate of recognition with model2.  # noqa: E501

        :param sentence_error_rate2: The sentence_error_rate2 of this EvaluationProperties.  # noqa: E501
        :type: float
        """

        self._sentence_error_rate2 = sentence_error_rate2

    @property
    def sentence_count2(self):
        """Gets the sentence_count2 of this EvaluationProperties.  # noqa: E501

        The number of processed sentences by model2.  # noqa: E501

        :return: The sentence_count2 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._sentence_count2

    @sentence_count2.setter
    def sentence_count2(self, sentence_count2):
        """Sets the sentence_count2 of this EvaluationProperties.

        The number of processed sentences by model2.  # noqa: E501

        :param sentence_count2: The sentence_count2 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._sentence_count2 = sentence_count2

    @property
    def word_count2(self):
        """Gets the word_count2 of this EvaluationProperties.  # noqa: E501

        The number of processed words by model2.  # noqa: E501

        :return: The word_count2 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_count2

    @word_count2.setter
    def word_count2(self, word_count2):
        """Sets the word_count2 of this EvaluationProperties.

        The number of processed words by model2.  # noqa: E501

        :param word_count2: The word_count2 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_count2 = word_count2

    @property
    def correct_word_count2(self):
        """Gets the correct_word_count2 of this EvaluationProperties.  # noqa: E501

        The number of correctly recognized words by model2.  # noqa: E501

        :return: The correct_word_count2 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._correct_word_count2

    @correct_word_count2.setter
    def correct_word_count2(self, correct_word_count2):
        """Sets the correct_word_count2 of this EvaluationProperties.

        The number of correctly recognized words by model2.  # noqa: E501

        :param correct_word_count2: The correct_word_count2 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._correct_word_count2 = correct_word_count2

    @property
    def word_substitution_count2(self):
        """Gets the word_substitution_count2 of this EvaluationProperties.  # noqa: E501

        The number of recognized words by model2, that are substitutions.  # noqa: E501

        :return: The word_substitution_count2 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_substitution_count2

    @word_substitution_count2.setter
    def word_substitution_count2(self, word_substitution_count2):
        """Sets the word_substitution_count2 of this EvaluationProperties.

        The number of recognized words by model2, that are substitutions.  # noqa: E501

        :param word_substitution_count2: The word_substitution_count2 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_substitution_count2 = word_substitution_count2

    @property
    def word_deletion_count2(self):
        """Gets the word_deletion_count2 of this EvaluationProperties.  # noqa: E501

        The number of recognized words by model2, that are deletions.  # noqa: E501

        :return: The word_deletion_count2 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_deletion_count2

    @word_deletion_count2.setter
    def word_deletion_count2(self, word_deletion_count2):
        """Sets the word_deletion_count2 of this EvaluationProperties.

        The number of recognized words by model2, that are deletions.  # noqa: E501

        :param word_deletion_count2: The word_deletion_count2 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_deletion_count2 = word_deletion_count2

    @property
    def word_insertion_count2(self):
        """Gets the word_insertion_count2 of this EvaluationProperties.  # noqa: E501

        The number of recognized words by model2, that are insertions.  # noqa: E501

        :return: The word_insertion_count2 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_insertion_count2

    @word_insertion_count2.setter
    def word_insertion_count2(self, word_insertion_count2):
        """Sets the word_insertion_count2 of this EvaluationProperties.

        The number of recognized words by model2, that are insertions.  # noqa: E501

        :param word_insertion_count2: The word_insertion_count2 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_insertion_count2 = word_insertion_count2

    @property
    def sentence_error_rate1(self):
        """Gets the sentence_error_rate1 of this EvaluationProperties.  # noqa: E501

        The sentence error rate of recognition with model1.  # noqa: E501

        :return: The sentence_error_rate1 of this EvaluationProperties.  # noqa: E501
        :rtype: float
        """
        return self._sentence_error_rate1

    @sentence_error_rate1.setter
    def sentence_error_rate1(self, sentence_error_rate1):
        """Sets the sentence_error_rate1 of this EvaluationProperties.

        The sentence error rate of recognition with model1.  # noqa: E501

        :param sentence_error_rate1: The sentence_error_rate1 of this EvaluationProperties.  # noqa: E501
        :type: float
        """

        self._sentence_error_rate1 = sentence_error_rate1

    @property
    def sentence_count1(self):
        """Gets the sentence_count1 of this EvaluationProperties.  # noqa: E501

        The number of processed sentences by model1.  # noqa: E501

        :return: The sentence_count1 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._sentence_count1

    @sentence_count1.setter
    def sentence_count1(self, sentence_count1):
        """Sets the sentence_count1 of this EvaluationProperties.

        The number of processed sentences by model1.  # noqa: E501

        :param sentence_count1: The sentence_count1 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._sentence_count1 = sentence_count1

    @property
    def word_count1(self):
        """Gets the word_count1 of this EvaluationProperties.  # noqa: E501

        The number of processed words by model1.  # noqa: E501

        :return: The word_count1 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_count1

    @word_count1.setter
    def word_count1(self, word_count1):
        """Sets the word_count1 of this EvaluationProperties.

        The number of processed words by model1.  # noqa: E501

        :param word_count1: The word_count1 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_count1 = word_count1

    @property
    def correct_word_count1(self):
        """Gets the correct_word_count1 of this EvaluationProperties.  # noqa: E501

        The number of correctly recognized words by model1.  # noqa: E501

        :return: The correct_word_count1 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._correct_word_count1

    @correct_word_count1.setter
    def correct_word_count1(self, correct_word_count1):
        """Sets the correct_word_count1 of this EvaluationProperties.

        The number of correctly recognized words by model1.  # noqa: E501

        :param correct_word_count1: The correct_word_count1 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._correct_word_count1 = correct_word_count1

    @property
    def word_substitution_count1(self):
        """Gets the word_substitution_count1 of this EvaluationProperties.  # noqa: E501

        The number of recognized words by model1, that are substitutions.  # noqa: E501

        :return: The word_substitution_count1 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_substitution_count1

    @word_substitution_count1.setter
    def word_substitution_count1(self, word_substitution_count1):
        """Sets the word_substitution_count1 of this EvaluationProperties.

        The number of recognized words by model1, that are substitutions.  # noqa: E501

        :param word_substitution_count1: The word_substitution_count1 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_substitution_count1 = word_substitution_count1

    @property
    def word_deletion_count1(self):
        """Gets the word_deletion_count1 of this EvaluationProperties.  # noqa: E501

        The number of recognized words by model1, that are deletions.  # noqa: E501

        :return: The word_deletion_count1 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_deletion_count1

    @word_deletion_count1.setter
    def word_deletion_count1(self, word_deletion_count1):
        """Sets the word_deletion_count1 of this EvaluationProperties.

        The number of recognized words by model1, that are deletions.  # noqa: E501

        :param word_deletion_count1: The word_deletion_count1 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_deletion_count1 = word_deletion_count1

    @property
    def word_insertion_count1(self):
        """Gets the word_insertion_count1 of this EvaluationProperties.  # noqa: E501

        The number of recognized words by model1, that are insertions.  # noqa: E501

        :return: The word_insertion_count1 of this EvaluationProperties.  # noqa: E501
        :rtype: int
        """
        return self._word_insertion_count1

    @word_insertion_count1.setter
    def word_insertion_count1(self, word_insertion_count1):
        """Sets the word_insertion_count1 of this EvaluationProperties.

        The number of recognized words by model1, that are insertions.  # noqa: E501

        :param word_insertion_count1: The word_insertion_count1 of this EvaluationProperties.  # noqa: E501
        :type: int
        """

        self._word_insertion_count1 = word_insertion_count1

    @property
    def email(self):
        """Gets the email of this EvaluationProperties.  # noqa: E501

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :return: The email of this EvaluationProperties.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EvaluationProperties.

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :param email: The email of this EvaluationProperties.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error(self):
        """Gets the error of this EvaluationProperties.  # noqa: E501


        :return: The error of this EvaluationProperties.  # noqa: E501
        :rtype: EntityError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EvaluationProperties.


        :param error: The error of this EvaluationProperties.  # noqa: E501
        :type: EntityError
        """

        self._error = error

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
        if issubclass(EvaluationProperties, dict):
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
        if not isinstance(other, EvaluationProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EvaluationProperties):
            return True

        return self.to_dict() != other.to_dict()
