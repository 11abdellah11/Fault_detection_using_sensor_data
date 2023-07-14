import pandas as pd


class Data_Getter_Pred:

    # Obtain data for prediction stage

    def __init__(self,file_object, logger_object):

        self.prediction_file = 'PredictionFromdb/InputFile.csv'
        self.file_object = file_object
        self.logger_object = logger_object

    def get_data(self):

        self.logger_object.log(self.file_object,'get data methode from data_getter_pred class')
        
        try:
            self.data = pd.read_csv(self.prediction_file)
            self.logger_object.log(self.file_object,'Reading completed')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured!')
            self.logger_object.log(self.file_object,'data load unsuccessful')

            raise Exception()
        