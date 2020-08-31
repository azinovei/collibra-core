# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from collibra_core.configuration import Configuration


class SetAssetAttributesRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type_id': 'str',
        'values': 'list[object]'
    }

    attribute_map = {
        'type_id': 'typeId',
        'values': 'values'
    }

    def __init__(self, type_id=None, values=None, local_vars_configuration=None):  # noqa: E501
        """SetAssetAttributesRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type_id = None
        self._values = None
        self.discriminator = None

        self.type_id = type_id
        self.values = values

    @property
    def type_id(self):
        """Gets the type_id of this SetAssetAttributesRequest.  # noqa: E501

        The ID of the attribute type for the new attribute.  # noqa: E501

        :return: The type_id of this SetAssetAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this SetAssetAttributesRequest.

        The ID of the attribute type for the new attribute.  # noqa: E501

        :param type_id: The type_id of this SetAssetAttributesRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def values(self):
        """Gets the values of this SetAssetAttributesRequest.  # noqa: E501

        The values for the new attribute.  # noqa: E501

        :return: The values of this SetAssetAttributesRequest.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this SetAssetAttributesRequest.

        The values for the new attribute.  # noqa: E501

        :param values: The values of this SetAssetAttributesRequest.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and values is None:  # noqa: E501
            raise ValueError("Invalid value for `values`, must not be `None`")  # noqa: E501

        self._values = values

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SetAssetAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetAssetAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()