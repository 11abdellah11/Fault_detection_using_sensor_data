# Fault_detection_using_sensordat


We will classify in this project if the wafer works or not, based on training data.
wafer : a wafer is a very thin slice or plate of single-crystal semiconductor material used to manufacture microelectronic components.

Dataset:
we have 500 sensors[590 columns] and a target column [ -1/O; bad/good], the first column represents types of wafers.


##Architecture and steps:

1- Data Ingestion:
  Batches for training / validation set / transformation(example : missed_data/none --> remove)/ exporting from the .csv file

2- Data clustering 
  (in order to increase the accuracy we will use different clusters and different models for each one...)
3- Get the best model for each cluster
4- Hyperparameter tuning and optimization
5-Pushing app to the cloud...( Azure)




folder architecture:

main.py
    Validation
    Training (rocessing,clustiring,





    
