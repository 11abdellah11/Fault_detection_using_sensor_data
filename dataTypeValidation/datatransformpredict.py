from datetime import datetime
from os import listdir
import pandas as pd
from application_logging import App_logger


# we will transform good training raw befor loading it in DB
class datatransformpredict:

    def __init__(self):
        self.goodDataPath = "Prediction_Rawfiles_Valid/Good_Raw"
        self.logger = App_logger()
    
    def replaceMissingWithNull(self):
        # here we will replace the missing box by NULL

        try:
            log_file = open('Prediction_Logs/dataTransformLog.txt','a+')
            onlyfiles = [f for f in listdir(self.goodDataPath)]
            for file in onlyfiles:
                csv = pd.read_csv(self.goodDataPath+'/'+file)
                csv.fillna('NULL',inplace=True) # we replace directly NaN by NULL et sans envoyer une copie     
                csv['Wafer'] = csv['Wafer'].str[6:]
                csv.to_csv(self.goodDataPath+'/'+file,index = None)
                self.logger.log(log_file," %s : transformation is done " %file )
        except Exception as e:
            
            self.logger.log(log_file,'transformation failed :(''')

            raise e
        
        log_file.close()
        