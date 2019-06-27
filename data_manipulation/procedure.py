# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:06:21 2019

@author: WentaoZhou
"""

import api_calls.procedure_calls as pc
import data_output as out
import medical_data_model.patient_procedure_model as ppm

def analyze_procedure_patient():
    """
    analyze procedure data and write them to external file
    """
    procedureData = pc.get_procedures()
    # refer to hdh api specification for its json structure
    procedures = procedureData["data"] 
    patientProcedures = []
    # loop through procedure instances
    for procedure in procedures:

# =============================================================================
#          patientProcedure = []
#          patientProcedure.append(procedure["id"])
#          patientProcedure.append(procedure["localId"])
#          patientProcedure.append(procedure["dataSource"])
#          
#          patientProcedures.append(patientProcedure)
# =============================================================================
        
         # collect data needed
         pp = ppm.PatientProcedure(procedure["id"], procedure["localId"],
                              procedure["dataSource"])
         
         patientProcedures.append(pp)
    
    # output data
    writeData(patientProcedures)

def writeData(source):
    """
    write data to a specified folder
    """
    # prepare output data
    data = [(i.procedureId, i.procedureLocalId, i.dataSource) 
                               for i in source]
    
    # file, e.g. excel, csv etc. headers
    columns = ['ProcedureId', 'ProcedureLocalId', 'DataSource']
    
    to_file = out.DataToExternalFile("../output/procedure-patient-sample2.xlsx")
    # write data
    to_file.writeDataToCsvWithPanda(data, columns);
    

if __name__ == '__main__':
    analyze_procedure_patient()