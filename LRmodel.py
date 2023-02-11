#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 18:26:39 2023

@author: rid
"""

from pyspark.ml import Pipeline
from pyspark.ml.feature import StopWordsRemover, Word2Vec, RegexTokenizer
from pyspark.ml.classification import LogisticRegression


def sentPipeline():
    #tokenize the text into words
    process1 = RegexTokenizer(inputCol = 'tweet', outputCol = 'tokens', pattern='\\W')
    #remove the unnecessary words
    process2 = StopWordsRemover(inputCol = 'tokens', outputCol = 'filtered')
    #vectorizing the list of words
    process3 = Word2Vec(inputCol = 'filtered', outputCol = 'vector')
    
    #logistic regression model
    model = LogisticRegression(featuresCol = 'vector', labelCol = 'label')
    
    #pipeline of the model
    pipeline = Pipeline(stages = [process1, process2, process3, model])
    
    return pipeline