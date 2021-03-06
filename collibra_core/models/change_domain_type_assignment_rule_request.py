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


class ChangeDomainTypeAssignmentRuleRequest(object):
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
        'domain_type_id': 'str',
        'community_id': 'str'
    }

    attribute_map = {
        'domain_type_id': 'domainTypeId',
        'community_id': 'communityId'
    }

    def __init__(self, domain_type_id=None, community_id=None, local_vars_configuration=None):  # noqa: E501
        """ChangeDomainTypeAssignmentRuleRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain_type_id = None
        self._community_id = None
        self.discriminator = None

        self.domain_type_id = domain_type_id
        if community_id is not None:
            self.community_id = community_id

    @property
    def domain_type_id(self):
        """Gets the domain_type_id of this ChangeDomainTypeAssignmentRuleRequest.  # noqa: E501

        The ID of the domain type the changed rule should refer to.  # noqa: E501

        :return: The domain_type_id of this ChangeDomainTypeAssignmentRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain_type_id

    @domain_type_id.setter
    def domain_type_id(self, domain_type_id):
        """Sets the domain_type_id of this ChangeDomainTypeAssignmentRuleRequest.

        The ID of the domain type the changed rule should refer to.  # noqa: E501

        :param domain_type_id: The domain_type_id of this ChangeDomainTypeAssignmentRuleRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and domain_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_type_id`, must not be `None`")  # noqa: E501

        self._domain_type_id = domain_type_id

    @property
    def community_id(self):
        """Gets the community_id of this ChangeDomainTypeAssignmentRuleRequest.  # noqa: E501

        The ID of the community the assignment rule should apply for.  # noqa: E501

        :return: The community_id of this ChangeDomainTypeAssignmentRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._community_id

    @community_id.setter
    def community_id(self, community_id):
        """Sets the community_id of this ChangeDomainTypeAssignmentRuleRequest.

        The ID of the community the assignment rule should apply for.  # noqa: E501

        :param community_id: The community_id of this ChangeDomainTypeAssignmentRuleRequest.  # noqa: E501
        :type: str
        """

        self._community_id = community_id

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
        if not isinstance(other, ChangeDomainTypeAssignmentRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeDomainTypeAssignmentRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
