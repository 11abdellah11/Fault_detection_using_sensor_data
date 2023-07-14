import pandas as pd

class Data_Getter:

    # class to obtain training data from source

    def __init__(self,file_object,logger_object):
        self.training_file = 'Training_FileFromdb/InputFile.csv'
        self.file_object = file_object
        self.logger_object = logger_object
    
    def get_data(self):
        # Reading data and then writing into panda file


        self.logger_object.log(self.file_object,'Starting of get_data method from Data_Getter class')

        try:
            self.data = pd.read_csv(self.training_file)
            self.logger_object.log(self.file_object, ' Reading copleted succefully!!')
            return self.data
        
        except Exception as e:
            self.logger_object.log(self.file_object,'Error while reading .csv data ')
            self.logger_object.log(self.file_object,'Data load unsuccessful.')

            raise Exception()
        