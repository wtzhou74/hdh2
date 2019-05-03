# -*- coding: utf-8 -*-

import pandas as pd
import csv
import procedure_calls as pc


class PatientProcedure:
    def __init__(self):
        self.procedureId = ""
        self.procedureLocalId = ""
        self.dataSource = ""
        self.dataSourceName = ""
        self.patientId = ""
        self.patientLocalId = ""
        self.last = ""
        self.middle = ""
        self.first = ""
        
def analyze_procedure_patient():
    procedureData = pc.get_procedures()
    procedures = procedureData["data"] 
    patientProcedures = []
    for procedure in procedures:
# =============================================================================
#         patientProcedure = PatientProcedure()
#         patientProcedure.procedureId = procedure["id"]
#         patientProcedure.procedureLocalId = procedure["localId"]
#         patientProcedure.dataSource = procedure["dataSource"]
# =============================================================================
        patientProcedure = []
        patientProcedure.append(procedure["id"])
        patientProcedure.append(procedure["localId"])
        patientProcedure.append(procedure["dataSource"])
        
        patientProcedures.append(patientProcedure)
        
    return patientProcedures


def writeDataToCsv():
    """
    write data to csv with python csv module
    """
    procedurePatients = analyze_procedure_patient()
    filename = 'procedure-patient-sample.csv'
    fields = ['ProcedureId', 'ProcedureLocalId', 'DataSource']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(procedurePatients)
        

def writeDataToCsvWithPanda():
    """
    write data to csv with Pandas
    """
    procedurePatients = analyze_procedure_patient()
    df = pd.DataFrame(procedurePatients, 
                      columns = ['ProcedureId', 'ProcedureLocalId', 'DataSource'])
    df.to_csv("procedure-patient-sample.csv", encoding='utf-8', index = False)

if __name__ == '__main__':
    # writeDataToCsv()
    writeDataToCsvWithPanda()
        