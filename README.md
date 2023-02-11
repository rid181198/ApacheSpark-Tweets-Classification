This is a basic logistic regression model of tweets classification of the racist comments. This is done on Apache Spark technology where the data streaming, data pipeline for the model have been implemented.

The script LRmodel.py generates the pre-processing pipelines for the text tokenization and vectorization with its logistic regression model. SparkInit.py script initializes the Spark context where the data schema is presented to load the training data. The last script StreamingData.py runs the Spark streaming of RDDs data from the server and predicts the racist comments from input tweets. 

To run the model, download the repository with the dataset. Using the terminal command, run the main script StreamingData.py by the following command,

python3 StreamingData.py localhost 8080

where localhost 8080 creates the system inbuilt server with the port number 8080. This will be transferred to the Spark streaming context to consider the text streams coming from this host server. You can also change the host name and port number which could give the inputs of tweets.

Simultaneously, to create the local server, run another command in a separate tab,

nc -lk 8080

and then input some texts which will be predicted by the running spark context. The project architecture is given as follows,

