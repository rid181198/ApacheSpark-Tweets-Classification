#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:51:40 2023

@author: rid
"""


from pyspark import SparkContext
from pyspark.sql.session import SparkSession
import pyspark.sql.types as tp



def sparkDataInit():
    #initilizing spark session
    sc = SparkContext(appName = "TweetClassfication")
    spark = SparkSession(sc)
    
    
    #schema to define the data types of input data
    Schema = tp.StructType([
        tp.StructField(name='id', dataType = tp.IntegerType(), nullable = True),
        tp.StructField(name = 'label', dataType = tp.IntegerType(), nullable = True),
        tp.StructField(name = 'tweet', dataType = tp.StringType(), nullable=True)
        ]
        )
    
    #importing the training dataset
    Data = spark.read.csv('./Dataset/twitter_sentiments.csv', schema = Schema, header = True)
    Data.printSchema()
    
    return Data, sc, spark
