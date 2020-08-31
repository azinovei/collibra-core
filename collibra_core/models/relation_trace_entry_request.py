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


class RelationTraceEntryRequest(object):
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
        'role_direction': 'bool',
        'relation_type_id': 'str'
    }

    attribute_map = {
        'role_direction': 'roleDirection',
        'relation_type_id': 'relationTypeId'
    }

    def __init__(self, role_direction=None, relation_type_id=None, local_vars_configuration=None):  # noqa: E501
        """RelationTraceEntryRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._role_direction = None
        self._relation_type_id = None
        self.discriminator = None

        if role_direction is not None:
            self.role_direction = role_direction
        self.relation_type_id = relation_type_id

    @property
    def role_direction(self):
        """Gets the role_direction of this RelationTraceEntryRequest.  # noqa: E501

        The direction of the relation to take, true if the relation is followed in role direction.  # noqa: E501

        :return: The role_direction of this RelationTraceEntryRequest.  # noqa: E501
        :rtype: bool
        """
        return self._role_direction

    @role_direction.setter
    def role_direction(self, role_direction):
        """Sets the role_direction of this RelationTraceEntryRequest.

        The direction of the relation to take, true if the relation is followed in role direction.  # noqa: E501

        :param role_direction: The role_direction of this RelationTraceEntryRequest.  # noqa: E501
        :type: bool
        """

        self._role_direction = role_direction

    @property
    def relation_type_id(self):
        """Gets the relation_type_id of this RelationTraceEntryRequest.  # noqa: E501

        The ID of the relation type for the relation trace entry.  # noqa: E501

        :return: The relation_type_id of this RelationTraceEntryRequest.  # noqa: E501
        :rtype: str
        """
        return self._relation_type_id

    @relation_type_id.setter
    def relation_type_id(self, relation_type_id):
        """Sets the relation_type_id of this RelationTraceEntryRequest.

        The ID of the relation type for the relation trace entry.  # noqa: E501

        :param relation_type_id: The relation_type_id of this RelationTraceEntryRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relation_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `relation_type_id`, must not be `None`")  # noqa: E501

        self._relation_type_id = relation_type_id

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
        if not isinstance(other, RelationTraceEntryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RelationTraceEntryRequest):
            return True

        return self.to_dict() != other.to_dict()