# -*- coding: utf-8 -*-

import constants
import general_call as gc

def get_procedures():
    """
    Call procedure API
    """
    api_uri = '{0}/procedures'.format(constants.API_URL_BASE)
    response = gc.call_hdh_api(api_uri)
    return response

# procedures = get_procedures()["data"]
# for procedure in procedures:
    # print(procedure["id"])
# type(procedures)
# df = pd.DataFrame(patients)
# print(df)