# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:05:00 2019

@author: WentaoZhou
"""

import general_call as gc
import constants

def get_patients():
    """
    call patient API
    """
    api_uri = '{0}/patients'.format(constants.API_URL_BASE)
    response = gc.call_hdh_api(api_uri)
    return response


# =============================================================================
# patients = get_patients()["data"]
# for patient in patients:
#     patient["id"]
# type(patients)
# df = pd.DataFrame(patients)
# print(df)
# =============================================================================

# flatten json by using pandas, referece to: 
# https://stackoverflow.com/questions/39899005/how-to-flatten-a-pandas-dataframe-with-some-columns-as-json
# df = pd.read_json(get_patient_info(), orient='columns')
# type(df)
# print(patients)
# df.to_csv('sample-patient.csv', encoding='utf-8')
