from sklearn.model_selection import train_test_split
from data_ingestion import data_loader
from data_preprocessing import preprocessing,clustering
from best_model_finder import tuner
from file_operations import file_methods
from application_logging import logger


class trainModel:
    def __init(self):
        self.log_writer = logger.App_logger()
        self.file_object = open('Training_logs/ModelTraining.txt')

    def trainingModel(self):

        #Logging start train
        self.log_writer.log(self.file_object,"start training....")
        try:
            # getting the data from the source.
            data_getter = data_loader.Data_Getter(self.file_object,self.log_writer)
            data = data_getter.get_data()

            # data preprocessing....
            X,Y = preprocesseur.is_null_present()
            is_null_present= preprocessor.is_null_present(X)

            # if missing values are ther we have to replace them
            if (is_null_present):
                X = preprocesseur.input_missing_values(X)
            # check the columns that not contribut to predictions, if std(column)==0 (i.e) the amount of variation is null (i.e) do not contribute to predictions.
            # so this columns have to be droped 
            columns_to_drop = preprocessor.get_columns_with_zero_std(X)

            #drop
            X = preprocessor.remove_columns(X,columns_to_drop)

            # Clustring
            #A fundamental step for any unsupervised algorithm is to determine the optimal number 
            # of clusters into which the data may be clustered. 
            # Since we do not have any predefined number of clusters in unsupervised learning.
            k_means = clustering.KMeansClustring(self.file_object,self.log_writer)
            number_of_clusters = k_means.elbow_plot(X) # In cluster analysis, the elbow method is a heuristic used
                                                        #in determining the number of clusters in a data set. The method consists of plotting
                                                        #  the explained variation as a function of the number of clusters and picking the elbow of
                                                        #  the curve as the number of clusters to use [[ pt fr flexion de la courbe]]

            # devide data into "k_means" clusters
            X = k_means.create_clusters(X,number_of_clusters)
            X['Labels'] = Y
            list_of_clusters = X['Cluster'].unique()

            # choose the best ML model to fit on individual cluster #

            for i in list_of_clusters:
                cluster_data=X[X['Cluster']==i] # filter the data for one cluster

                # Prepare the feature and Label columns
                cluster_features=cluster_data.drop(['Labels','Cluster'],axis=1)
                cluster_label= cluster_data['Labels']

                # splitting the data into training and test set for each cluster one by one
                x_train, x_test, y_train, y_test = train_test_split(cluster_features, cluster_label, test_size=1 / 3, random_state=355)

                model_finder=tuner.Model_Finder(self.file_object,self.log_writer) # object initialization

                #getting the best model for each of the clusters
                best_model_name,best_model=model_finder.get_best_model(x_train,y_train,x_test,y_test)

                #saving the best model to the directory.
                file_op = file_methods.File_Operation(self.file_object,self.log_writer)
                save_model=file_op.save_model(best_model,best_model_name+str(i))

            # logging the successful Training
            self.log_writer.log(self.file_object, 'Successful End of Training')
            self.file_object.close()

        except Exception:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception