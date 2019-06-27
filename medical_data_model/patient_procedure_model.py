# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:21:08 2019

@author: WentaoZhou
"""

# =============================================================================
# class PatientProcedure:
#     def __init__(self, procedureId='', procedureLocalId='', description='',
#                  dataSource='', dataSourceName='', patientId='', 
#                  patientLocalId='', first='', middle='', last='', dob=''):
#         self.procedureId = procedureId
#         self.procedureLocalId = procedureLocalId
#         self.dataSource = dataSource
#         self.dataSourceName = dataSourceName
#         self.patientId = patientId
#         self.patientLocalId = patientLocalId
#         self.last = last
#         self.middle = middle
#         self.first = first
#         self.dob = dob
# =============================================================================

class PatientProcedure():
    """
    data model for specific purpose, e.g. report
    """
    # class_attribute;
    
    def __init__(self, procedureId='', procedureLocalId='',
                 dataSource=''):
        # instance attributes
        self.procedureId = procedureId
        self.procedureLocalId = procedureLocalId
        self.dataSource = dataSource