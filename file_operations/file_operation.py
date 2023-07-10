import pickle
import os 
import shutil



class File_Operation:


    def __init__(self,file_object,logger_object):

        self.file_object = file_object
        self.logger_object = logger_object
        self.model_directory = 'models/'


    def save_model(self, model, filename):
        
        self.logger_object.log(self.file_object,'Saving model...')
        try:
            path = os.path.join(self.model_directory,filename)
            if os.path.isdir(path):
                shutil.rmtree(self.model_directory)# delete previous model for each cluster
                os.makedirs(path)
            else: 
                os.makedirs(path)
            with open(path + '/' + filename + '.sav', 'wb') as f:
                pickle.dump(model,f)
                self.logger_object.log(self.file_object, 'Model File' + filename + 'saved')
                return 'success'
            
        except Exception as e:
            self.logger_object.log(self.file_object,'Error while saving the model')
            self.logger_object.log(self.file_object,'Model file '+filename +' Could not be saved')

            raise e
        

    def load_model(self,filename):
        self.logger_object.log(self.file_object,' Loading the model')
        try:
            with open(self.model_directory + '/'+ filename + '.sav') as f:
                self.logger_object.log(self.file_object,'Model file' + filename + 'Loaded')
                return pickle.load(f)
        except Exception as e:
            self.logger_object.log(self.file_object,'Error while loading the model.' + filename)

            raise e
        
    def find_correct_model_file(self,cluster_number):

        self.logger_object.log(self.file_object,'Searching the correct models for each cluster')
        try:
            self.cluster_number = cluster_number
            self.folder_name = self.model_directory
            self.list_of_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    if self.file.index(str(self.cluster_number)) !=-1 : # check if the file contain the cluster number 
                        self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            self.logger_object.log(self.file_object,'the model'+ self.model_name + 'exist')

            return self.model_name
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured while search the correct model ')
            

            raise Exception()
        