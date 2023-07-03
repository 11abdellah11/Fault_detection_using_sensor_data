from datetime import datetime
from prediction_raw_data_val.prediction_val_data import Predictiondata_val
from application_logging import logger
from datatransformation_pred.datatransformpredict import datatransformpredict
from datatransformation_pred.datatransformpredict import dBOperation

class pred_validition:
    def __init__(self,path):
        self.raw_data = Predictiondata_val(path)
        self.datatransform = datatransformpredict()
        self.dBOperation = dBOperation()
        self.file_object = open("Prediction_logs/pred_log.txt",'a+') # en mode append
        self.log_writter = logger.App_logger()

    def prediction_validation(self):
        try:
            self.log_writer.log(self.file_object,'Start of validation on files')
            LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,noofcolumns = self.raw_data.valuesFromSchema()#extracting information from prediciton
            regex = self.raw_data.manualRegexCreation() # GETTING the regex defined to validate filename
            self.raw_data.validationFileNameRaw(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)
            self.raw_data.validateColumnLength(noofcolumns)#validating nbr of column
            self.raw_data.validateMissingValuesInwholeColumn()#check if a column contain missing values
            self.log_writer.log(self.file_object,"Checking raw data Finish")

            #Transf. data ( we will just replace blanks by NULL)
            self.log_writter.log(self.file_object," Data transformation start:")
            self.datatransform.ReplaceMissingWithNull()
            self.log_writterLog(self.file_object,"Transformation complete")

            # creation of prediction dB
            self.log_writter.log(self.file_object,"Creation of a set like in the given schema:")
            self.dBOperation.createTableDb('Prediction',column_names)
            self.log_writter.log(self.file_object,"Tableau crée.")
            self.log_writter.log(self.file_object,"Insertion of data  into table :")
            self.log_writter.log(self.file_object,'DELETING GOODdata Folder.')
            
            # after loading, delete good data folder
            self.raw_data.deleteExistingGoodDataTrainingFolder()
            self.log_writter.log(self.file_object,"deleting good Data foleder.")
            self.log_writter.log(self.file_object,"Moving bad files to archive !")
            
            # Move bad files to archive folder
            self.raw_data.moveBadFilesToArchiveBad()
            self.log_writter.log(self.file_object,"bad files moved and bad folder deleted")
            self.log_writter.log(self.file_object,"validation finish")
            self.log_writter.log(self.file_object,'extracting csv file from table')
            
            #export data in table .csv
            self.dBOperation.selectingDatafromtableintocsv()


        except Exception as e:
            raise e
