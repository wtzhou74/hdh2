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
        patientProcedure = PatientProcedure()
        patientProcedure.procedureId = procedure["id"]
        patientProcedure.procedureLocalId = procedure["localId"]
        patientProcedure.dataSource = procedure["dataSource"]
        
        patientProcedures.append(patientProcedure)
        
    return patientProcedures


def writeDataToCsv():
    procedurePatients = analyze_procedure_patient()
    filename = 'procedure-patient-sample.csv'
    fields = ['procedureId', 'procedureLocalId', 'dataSource']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(procedurePatients)
    # df = pd.DataFrame(procedurePatients)
    # df.to_csv("procedure-patient-sample.csv", encoding='utf-8')


if __name__ == '__main__':
    writeDataToCsv()
        