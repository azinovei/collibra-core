# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from collibra_core.api_client import ApiClient
from collibra_core.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ResponsibilitiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_responsibilities(self, **kwargs):  # noqa: E501
        """Adds multiple responsibilities in one go.  # noqa: E501

        Adds multiple responsibilities in one go. Assigns the given users to the resources with the given roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_responsibilities(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[AddResponsibilityRequest] add_responsibility_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[ResponsibilityImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_responsibilities_with_http_info(**kwargs)  # noqa: E501

    def add_responsibilities_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple responsibilities in one go.  # noqa: E501

        Adds multiple responsibilities in one go. Assigns the given users to the resources with the given roles.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_responsibilities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[AddResponsibilityRequest] add_responsibility_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[ResponsibilityImpl], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'add_responsibility_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_responsibilities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add_responsibility_request' in local_var_params:
            body_params = local_var_params['add_responsibility_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/responsibilities/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ResponsibilityImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def add_responsibility(self, **kwargs):  # noqa: E501
        """Adds a new responsibility.  # noqa: E501

        Adds new responsibility. Assigns given user to resource with given role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_responsibility(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddResponsibilityRequest add_responsibility_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResponsibilityImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_responsibility_with_http_info(**kwargs)  # noqa: E501

    def add_responsibility_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new responsibility.  # noqa: E501

        Adds new responsibility. Assigns given user to resource with given role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_responsibility_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddResponsibilityRequest add_responsibility_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResponsibilityImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'add_responsibility_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_responsibility" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add_responsibility_request' in local_var_params:
            body_params = local_var_params['add_responsibility_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/responsibilities', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsibilityImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_responsibilities(self, **kwargs):  # noqa: E501
        """Finds responsibilities.  # noqa: E501

        Returns responsibilities matching the given search criteria.  Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned responsibilities satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 responsibilities is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_responsibilities(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param list[str] resource_ids: The list of IDs of the resources for which the responsibilities should be found.
        :param list[str] owner_ids: The list of IDs of the owners for which the responsibilities should be found.
        :param list[str] role_ids: The list of IDs of the roles for which the responsibilities should be found.
        :param bool include_inherited: Whether inherited responsibilities should be included in the search results.
        :param bool global_only: Whether only global responsibilities should be searched.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param str type: Indicates which type of responsibilities should be searched for. Usage is mutually exclusive with the deprecated globalOnly flag.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedResponseResponsibility
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_responsibilities_with_http_info(**kwargs)  # noqa: E501

    def find_responsibilities_with_http_info(self, **kwargs):  # noqa: E501
        """Finds responsibilities.  # noqa: E501

        Returns responsibilities matching the given search criteria.  Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned responsibilities satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 responsibilities is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_responsibilities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param list[str] resource_ids: The list of IDs of the resources for which the responsibilities should be found.
        :param list[str] owner_ids: The list of IDs of the owners for which the responsibilities should be found.
        :param list[str] role_ids: The list of IDs of the roles for which the responsibilities should be found.
        :param bool include_inherited: Whether inherited responsibilities should be included in the search results.
        :param bool global_only: Whether only global responsibilities should be searched.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param str type: Indicates which type of responsibilities should be searched for. Usage is mutually exclusive with the deprecated globalOnly flag.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedResponseResponsibility, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'resource_ids',
            'owner_ids',
            'role_ids',
            'include_inherited',
            'global_only',
            'sort_field',
            'sort_order',
            'type'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_responsibilities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'resource_ids' in local_var_params and local_var_params['resource_ids'] is not None:  # noqa: E501
            query_params.append(('resourceIds', local_var_params['resource_ids']))  # noqa: E501
            collection_formats['resourceIds'] = 'multi'  # noqa: E501
        if 'owner_ids' in local_var_params and local_var_params['owner_ids'] is not None:  # noqa: E501
            query_params.append(('ownerIds', local_var_params['owner_ids']))  # noqa: E501
            collection_formats['ownerIds'] = 'multi'  # noqa: E501
        if 'role_ids' in local_var_params and local_var_params['role_ids'] is not None:  # noqa: E501
            query_params.append(('roleIds', local_var_params['role_ids']))  # noqa: E501
            collection_formats['roleIds'] = 'multi'  # noqa: E501
        if 'include_inherited' in local_var_params and local_var_params['include_inherited'] is not None:  # noqa: E501
            query_params.append(('includeInherited', local_var_params['include_inherited']))  # noqa: E501
        if 'global_only' in local_var_params and local_var_params['global_only'] is not None:  # noqa: E501
            query_params.append(('globalOnly', local_var_params['global_only']))  # noqa: E501
        if 'sort_field' in local_var_params and local_var_params['sort_field'] is not None:  # noqa: E501
            query_params.append(('sortField', local_var_params['sort_field']))  # noqa: E501
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/responsibilities', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponseResponsibility',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_responsibility(self, responsibility_id, **kwargs):  # noqa: E501
        """Returns the responsibility identified by the given id.  # noqa: E501

        Returns the responsibility identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_responsibility(responsibility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str responsibility_id: The unique identifier of the responsibility. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResponsibilityImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_responsibility_with_http_info(responsibility_id, **kwargs)  # noqa: E501

    def get_responsibility_with_http_info(self, responsibility_id, **kwargs):  # noqa: E501
        """Returns the responsibility identified by the given id.  # noqa: E501

        Returns the responsibility identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_responsibility_with_http_info(responsibility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str responsibility_id: The unique identifier of the responsibility. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResponsibilityImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'responsibility_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_responsibility" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'responsibility_id' is set
        if self.api_client.client_side_validation and ('responsibility_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['responsibility_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `responsibility_id` when calling `get_responsibility`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'responsibility_id' in local_var_params:
            path_params['responsibilityId'] = local_var_params['responsibility_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/responsibilities/{responsibilityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsibilityImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_responsibilities(self, **kwargs):  # noqa: E501
        """Removes multiple responsibilities in one go.  # noqa: E501

        Removes multiple responsibilities in one go identified by given ids.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_responsibilities(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] request_body: The unique identifiers of the responsibilities.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.remove_responsibilities_with_http_info(**kwargs)  # noqa: E501

    def remove_responsibilities_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple responsibilities in one go.  # noqa: E501

        Removes multiple responsibilities in one go identified by given ids.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_responsibilities_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[str] request_body: The unique identifiers of the responsibilities.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'request_body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_responsibilities" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request_body' in local_var_params:
            body_params = local_var_params['request_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/responsibilities/bulk', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_responsibility(self, responsibility_id, **kwargs):  # noqa: E501
        """Removes the responsibility identified by the given id.  # noqa: E501

        Removes the responsibility identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_responsibility(responsibility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str responsibility_id: The unique identifier of the responsibility. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.remove_responsibility_with_http_info(responsibility_id, **kwargs)  # noqa: E501

    def remove_responsibility_with_http_info(self, responsibility_id, **kwargs):  # noqa: E501
        """Removes the responsibility identified by the given id.  # noqa: E501

        Removes the responsibility identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_responsibility_with_http_info(responsibility_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str responsibility_id: The unique identifier of the responsibility. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'responsibility_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_responsibility" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'responsibility_id' is set
        if self.api_client.client_side_validation and ('responsibility_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['responsibility_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `responsibility_id` when calling `remove_responsibility`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'responsibility_id' in local_var_params:
            path_params['responsibilityId'] = local_var_params['responsibility_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/responsibilities/{responsibilityId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)