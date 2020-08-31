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


class ComplexRelationLegRequest(object):
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
        'leg_type_id': 'str',
        'asset_id': 'str'
    }

    attribute_map = {
        'leg_type_id': 'legTypeId',
        'asset_id': 'assetId'
    }

    def __init__(self, leg_type_id=None, asset_id=None, local_vars_configuration=None):  # noqa: E501
        """ComplexRelationLegRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._leg_type_id = None
        self._asset_id = None
        self.discriminator = None

        self.leg_type_id = leg_type_id
        self.asset_id = asset_id

    @property
    def leg_type_id(self):
        """Gets the leg_type_id of this ComplexRelationLegRequest.  # noqa: E501

        The ID of the type of the single leg for complex relation.  # noqa: E501

        :return: The leg_type_id of this ComplexRelationLegRequest.  # noqa: E501
        :rtype: str
        """
        return self._leg_type_id

    @leg_type_id.setter
    def leg_type_id(self, leg_type_id):
        """Sets the leg_type_id of this ComplexRelationLegRequest.

        The ID of the type of the single leg for complex relation.  # noqa: E501

        :param leg_type_id: The leg_type_id of this ComplexRelationLegRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and leg_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `leg_type_id`, must not be `None`")  # noqa: E501

        self._leg_type_id = leg_type_id

    @property
    def asset_id(self):
        """Gets the asset_id of this ComplexRelationLegRequest.  # noqa: E501

        The ID of the asset attached to the leg of the complex relation.  # noqa: E501

        :return: The asset_id of this ComplexRelationLegRequest.  # noqa: E501
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ComplexRelationLegRequest.

        The ID of the asset attached to the leg of the complex relation.  # noqa: E501

        :param asset_id: The asset_id of this ComplexRelationLegRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and asset_id is None:  # noqa: E501
            raise ValueError("Invalid value for `asset_id`, must not be `None`")  # noqa: E501

        self._asset_id = asset_id

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
        if not isinstance(other, ComplexRelationLegRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComplexRelationLegRequest):
            return True

        return self.to_dict() != other.to_dict()