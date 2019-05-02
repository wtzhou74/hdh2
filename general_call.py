# -*- coding: utf-8 -*-

import json
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

import constants

def call_hdh_api(api_uri):
    """
    call API to get data
    """
    response = requests.get(api_uri, headers=constants.HEADERS, 
                            auth=HTTPBasicAuth(constants.HDH_USER_NAME, constants.PASSWORD))
    
    if response.status_code == 200:
        print('success to reach patient api')
        # print(type(response.content.decode('utf-8'))) # json string
        return json.loads(response.content.decode('utf-8')) # dict
        # return response.content.decode('utf-8')
    elif response.status_code >= 500:
        print('[!] [{0}] Internal Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_uri))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(response.content )
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None