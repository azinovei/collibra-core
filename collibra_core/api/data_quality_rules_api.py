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


class DataQualityRulesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_data_quality_rule(self, **kwargs):  # noqa: E501
        """Adds a new data quality rule.  # noqa: E501

        Adds a new data quality rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_data_quality_rule(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddDataQualityRuleRequest add_data_quality_rule_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DataQualityRuleImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_data_quality_rule_with_http_info(**kwargs)  # noqa: E501

    def add_data_quality_rule_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new data quality rule.  # noqa: E501

        Adds a new data quality rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_data_quality_rule_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddDataQualityRuleRequest add_data_quality_rule_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DataQualityRuleImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'add_data_quality_rule_request'
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
                    " to method add_data_quality_rule" % key
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
        if 'add_data_quality_rule_request' in local_var_params:
            body_params = local_var_params['add_data_quality_rule_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dataQualityRules', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataQualityRuleImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_data_quality_rule(self, data_quality_rule_id, **kwargs):  # noqa: E501
        """Changes the data quality rule with the information that is present in the request.  # noqa: E501

        Changes the data quality rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_data_quality_rule(data_quality_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_quality_rule_id: the unique identifier of the data quality rule (required)
        :param ChangeDataQualityRuleRequest change_data_quality_rule_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DataQualityRuleImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.change_data_quality_rule_with_http_info(data_quality_rule_id, **kwargs)  # noqa: E501

    def change_data_quality_rule_with_http_info(self, data_quality_rule_id, **kwargs):  # noqa: E501
        """Changes the data quality rule with the information that is present in the request.  # noqa: E501

        Changes the data quality rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_data_quality_rule_with_http_info(data_quality_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_quality_rule_id: the unique identifier of the data quality rule (required)
        :param ChangeDataQualityRuleRequest change_data_quality_rule_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DataQualityRuleImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_quality_rule_id',
            'change_data_quality_rule_request'
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
                    " to method change_data_quality_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_quality_rule_id' is set
        if self.api_client.client_side_validation and ('data_quality_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_quality_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_quality_rule_id` when calling `change_data_quality_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_quality_rule_id' in local_var_params:
            path_params['dataQualityRuleId'] = local_var_params['data_quality_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'change_data_quality_rule_request' in local_var_params:
            body_params = local_var_params['change_data_quality_rule_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dataQualityRules/{dataQualityRuleId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataQualityRuleImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_data_quality_rules(self, **kwargs):  # noqa: E501
        """Returns data quality rules matching the given search criteria.  # noqa: E501

        Returns data quality rules matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned data quality rules satisfy all constraints that are specified in this search criteria. By default a result containing 1000 data quality rules is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_data_quality_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str name: The name of the dataquality rule to search for.
        :param str name_match_mode: The match mode used to compare <code>name</code>.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DataQualityRulePagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_data_quality_rules_with_http_info(**kwargs)  # noqa: E501

    def find_data_quality_rules_with_http_info(self, **kwargs):  # noqa: E501
        """Returns data quality rules matching the given search criteria.  # noqa: E501

        Returns data quality rules matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned data quality rules satisfy all constraints that are specified in this search criteria. By default a result containing 1000 data quality rules is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_data_quality_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str name: The name of the dataquality rule to search for.
        :param str name_match_mode: The match mode used to compare <code>name</code>.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DataQualityRulePagedResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'name',
            'name_match_mode',
            'sort_field',
            'sort_order'
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
                    " to method find_data_quality_rules" % key
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
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name_match_mode' in local_var_params and local_var_params['name_match_mode'] is not None:  # noqa: E501
            query_params.append(('nameMatchMode', local_var_params['name_match_mode']))  # noqa: E501
        if 'sort_field' in local_var_params and local_var_params['sort_field'] is not None:  # noqa: E501
            query_params.append(('sortField', local_var_params['sort_field']))  # noqa: E501
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501

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
            '/dataQualityRules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataQualityRulePagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_data_quality_rule(self, data_quality_rule_id, **kwargs):  # noqa: E501
        """Returns the DataQualityRule identified by given id.  # noqa: E501

        Returns the DataQualityRule identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_quality_rule(data_quality_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_quality_rule_id: the unique identifier of the data quality rule (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DataQualityRuleImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_data_quality_rule_with_http_info(data_quality_rule_id, **kwargs)  # noqa: E501

    def get_data_quality_rule_with_http_info(self, data_quality_rule_id, **kwargs):  # noqa: E501
        """Returns the DataQualityRule identified by given id.  # noqa: E501

        Returns the DataQualityRule identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_data_quality_rule_with_http_info(data_quality_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_quality_rule_id: the unique identifier of the data quality rule (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DataQualityRuleImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'data_quality_rule_id'
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
                    " to method get_data_quality_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_quality_rule_id' is set
        if self.api_client.client_side_validation and ('data_quality_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_quality_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_quality_rule_id` when calling `get_data_quality_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_quality_rule_id' in local_var_params:
            path_params['dataQualityRuleId'] = local_var_params['data_quality_rule_id']  # noqa: E501

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
            '/dataQualityRules/{dataQualityRuleId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataQualityRuleImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_data_quality_rule(self, data_quality_rule_id, **kwargs):  # noqa: E501
        """Removes the DataQualityRule identified by the given id.  # noqa: E501

        Removes the DataQualityRule identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_data_quality_rule(data_quality_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_quality_rule_id: the unique identifier of the data quality rule (required)
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
        return self.remove_data_quality_rule_with_http_info(data_quality_rule_id, **kwargs)  # noqa: E501

    def remove_data_quality_rule_with_http_info(self, data_quality_rule_id, **kwargs):  # noqa: E501
        """Removes the DataQualityRule identified by the given id.  # noqa: E501

        Removes the DataQualityRule identified by the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_data_quality_rule_with_http_info(data_quality_rule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str data_quality_rule_id: the unique identifier of the data quality rule (required)
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
            'data_quality_rule_id'
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
                    " to method remove_data_quality_rule" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data_quality_rule_id' is set
        if self.api_client.client_side_validation and ('data_quality_rule_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['data_quality_rule_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data_quality_rule_id` when calling `remove_data_quality_rule`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'data_quality_rule_id' in local_var_params:
            path_params['dataQualityRuleId'] = local_var_params['data_quality_rule_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dataQualityRules/{dataQualityRuleId}', 'DELETE',
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
