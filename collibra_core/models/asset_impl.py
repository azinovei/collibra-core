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


class AssetImpl(object):
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
        'id': 'str',
        'created_by': 'str',
        'created_on': 'int',
        'last_modified_by': 'str',
        'last_modified_on': 'int',
        'system': 'bool',
        'resource_type': 'str',
        'name': 'str',
        'display_name': 'str',
        'articulation_score': 'float',
        'excluded_from_auto_hyperlinking': 'bool',
        'domain': 'NamedResourceReferenceImpl',
        'type': 'NamedResourceReferenceImpl',
        'status': 'NamedResourceReferenceImpl',
        'avg_rating': 'float',
        'ratings_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'name': 'name',
        'display_name': 'displayName',
        'articulation_score': 'articulationScore',
        'excluded_from_auto_hyperlinking': 'excludedFromAutoHyperlinking',
        'domain': 'domain',
        'type': 'type',
        'status': 'status',
        'avg_rating': 'avgRating',
        'ratings_count': 'ratingsCount'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, name=None, display_name=None, articulation_score=None, excluded_from_auto_hyperlinking=None, domain=None, type=None, status=None, avg_rating=None, ratings_count=None, local_vars_configuration=None):  # noqa: E501
        """AssetImpl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._name = None
        self._display_name = None
        self._articulation_score = None
        self._excluded_from_auto_hyperlinking = None
        self._domain = None
        self._type = None
        self._status = None
        self._avg_rating = None
        self._ratings_count = None
        self.discriminator = None

        self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if system is not None:
            self.system = system
        self.resource_type = resource_type
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if articulation_score is not None:
            self.articulation_score = articulation_score
        if excluded_from_auto_hyperlinking is not None:
            self.excluded_from_auto_hyperlinking = excluded_from_auto_hyperlinking
        if domain is not None:
            self.domain = domain
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if avg_rating is not None:
            self.avg_rating = avg_rating
        if ratings_count is not None:
            self.ratings_count = ratings_count

    @property
    def id(self):
        """Gets the id of this AssetImpl.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this AssetImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetImpl.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this AssetImpl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this AssetImpl.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this AssetImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AssetImpl.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this AssetImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this AssetImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this AssetImpl.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AssetImpl.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this AssetImpl.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this AssetImpl.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this AssetImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this AssetImpl.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this AssetImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this AssetImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this AssetImpl.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this AssetImpl.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this AssetImpl.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this AssetImpl.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this AssetImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this AssetImpl.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this AssetImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this AssetImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this AssetImpl.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this AssetImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this AssetImpl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this AssetImpl.  # noqa: E501

        The name of the resource.  # noqa: E501

        :return: The name of this AssetImpl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetImpl.

        The name of the resource.  # noqa: E501

        :param name: The name of this AssetImpl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this AssetImpl.  # noqa: E501

        The display name of the asset.  <p>  Please note that \"displayName\" corresponds to the \"Name\" in the UI.  # noqa: E501

        :return: The display_name of this AssetImpl.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AssetImpl.

        The display name of the asset.  <p>  Please note that \"displayName\" corresponds to the \"Name\" in the UI.  # noqa: E501

        :param display_name: The display_name of this AssetImpl.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def articulation_score(self):
        """Gets the articulation_score of this AssetImpl.  # noqa: E501

        The articulation score for this asset.  <p>  Expresses how well this asset is articulated.  The articulation score is a percentage number ranging from 0 to 100.  The articulation rules can be configured to calculate the articulation score.  Whenever the asset is modified, by changing its attributes or statuses, the articulation score is re-evaluated.  # noqa: E501

        :return: The articulation_score of this AssetImpl.  # noqa: E501
        :rtype: float
        """
        return self._articulation_score

    @articulation_score.setter
    def articulation_score(self, articulation_score):
        """Sets the articulation_score of this AssetImpl.

        The articulation score for this asset.  <p>  Expresses how well this asset is articulated.  The articulation score is a percentage number ranging from 0 to 100.  The articulation rules can be configured to calculate the articulation score.  Whenever the asset is modified, by changing its attributes or statuses, the articulation score is re-evaluated.  # noqa: E501

        :param articulation_score: The articulation_score of this AssetImpl.  # noqa: E501
        :type: float
        """

        self._articulation_score = articulation_score

    @property
    def excluded_from_auto_hyperlinking(self):
        """Gets the excluded_from_auto_hyperlinking of this AssetImpl.  # noqa: E501

        Whether this asset is excluded from hyperlinking or not.  # noqa: E501

        :return: The excluded_from_auto_hyperlinking of this AssetImpl.  # noqa: E501
        :rtype: bool
        """
        return self._excluded_from_auto_hyperlinking

    @excluded_from_auto_hyperlinking.setter
    def excluded_from_auto_hyperlinking(self, excluded_from_auto_hyperlinking):
        """Sets the excluded_from_auto_hyperlinking of this AssetImpl.

        Whether this asset is excluded from hyperlinking or not.  # noqa: E501

        :param excluded_from_auto_hyperlinking: The excluded_from_auto_hyperlinking of this AssetImpl.  # noqa: E501
        :type: bool
        """

        self._excluded_from_auto_hyperlinking = excluded_from_auto_hyperlinking

    @property
    def domain(self):
        """Gets the domain of this AssetImpl.  # noqa: E501


        :return: The domain of this AssetImpl.  # noqa: E501
        :rtype: NamedResourceReferenceImpl
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AssetImpl.


        :param domain: The domain of this AssetImpl.  # noqa: E501
        :type: NamedResourceReferenceImpl
        """

        self._domain = domain

    @property
    def type(self):
        """Gets the type of this AssetImpl.  # noqa: E501


        :return: The type of this AssetImpl.  # noqa: E501
        :rtype: NamedResourceReferenceImpl
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssetImpl.


        :param type: The type of this AssetImpl.  # noqa: E501
        :type: NamedResourceReferenceImpl
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this AssetImpl.  # noqa: E501


        :return: The status of this AssetImpl.  # noqa: E501
        :rtype: NamedResourceReferenceImpl
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssetImpl.


        :param status: The status of this AssetImpl.  # noqa: E501
        :type: NamedResourceReferenceImpl
        """

        self._status = status

    @property
    def avg_rating(self):
        """Gets the avg_rating of this AssetImpl.  # noqa: E501

        The average rating.  # noqa: E501

        :return: The avg_rating of this AssetImpl.  # noqa: E501
        :rtype: float
        """
        return self._avg_rating

    @avg_rating.setter
    def avg_rating(self, avg_rating):
        """Sets the avg_rating of this AssetImpl.

        The average rating.  # noqa: E501

        :param avg_rating: The avg_rating of this AssetImpl.  # noqa: E501
        :type: float
        """

        self._avg_rating = avg_rating

    @property
    def ratings_count(self):
        """Gets the ratings_count of this AssetImpl.  # noqa: E501

        The number of ratings.  # noqa: E501

        :return: The ratings_count of this AssetImpl.  # noqa: E501
        :rtype: int
        """
        return self._ratings_count

    @ratings_count.setter
    def ratings_count(self, ratings_count):
        """Sets the ratings_count of this AssetImpl.

        The number of ratings.  # noqa: E501

        :param ratings_count: The ratings_count of this AssetImpl.  # noqa: E501
        :type: int
        """

        self._ratings_count = ratings_count

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
        if not isinstance(other, AssetImpl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetImpl):
            return True

        return self.to_dict() != other.to_dict()