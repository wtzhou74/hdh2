# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:04:16 2019

@author: WentaoZhou
"""

from data_manipulation import procedure
import pandas as pd
import csv

class DataToExternalFile:
    """
    write data to specified place
    """
    def __init__(self, path):
        self.path = path
        
    # functions
    def writeDataToCsvWithPanda(self, source, columns):
        """
        write data to csv with Pandas
        :type source: list
        :type columns: list
        """
         
        # convert list to dataframe
        df = pd.DataFrame(source, columns=columns)
        
        # write data to external excel file
        df.to_excel(self.path, encoding='utf-8', index = False)
        
        
    def writeDataToCsv(self):
        """
        write data to csv with python csv module
        """
        procedurePatients = procedure.analyze_procedure_patient()
        filename = 'procedure-patient-sample.csv'
        fields = ['ProcedureId', 'ProcedureLocalId', 'DataSource']
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerows(procedurePatients)
    
        