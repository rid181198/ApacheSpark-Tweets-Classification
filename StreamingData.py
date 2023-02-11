#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:27:34 2023

@author: rid
"""

from LRmodel import sentPipeline
from SparkInit import sparkDataInit
from pyspark.streaming import StreamingContext
from pyspark.sql import Row
import sys

#prediction 
def get_prediction(tweetText):
    try:
        #only considering tweets with length greater than 0
        tweetText = tweetText.filter(lambda x: len(x)>0)
        
        #creating the dataframe
        rowCol = tweetText.map(lambda w: Row(tweet=w))
        
        #dataframe in spark
        sparkDf = spark.createDataFrame(rowCol)
        
        #transform the data and prediction
        pipelineFit.transform(sparkDf).select('tweet','prediction').show()
    
    except:
        print('No data')
    
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("No host number and port number", file = sys.stderr)
        sys.exit(-1)
        
    print('\nLoading the data......')
    sparkData, sc, spark = sparkDataInit()
    
    print('\nLoading the pipeline.....')
    pipeline = sentPipeline()
    
    print('\nfit the model.....')
    pipelineFit = pipeline.fit(sparkData)


    print('\nModel is trained!')
    print('\nWaiting for the data....')
    print(sys.argv[1],int(sys.argv[2]))
    
    #initializing the streaming data
    ssc = StreamingContext(sc, batchDuration = 3)
    lines = ssc.socketTextStream(sys.argv[1],int(sys.argv[2]))
    
    words = lines.flatMap(lambda line: line.split('TWEET_APP'))
    
    words.foreachRDD(get_prediction)
    
    ssc.start()
    ssc.awaitTermination()
    
