'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    # TODO
    cols=df.keys()[-1]
    vals=df[cols].unique()
    entropy=0
    for i in vals:
        entropy+= -(df[cols].value_counts()[i]/len(df[cols]))* np.log2(df[cols].value_counts()[i]/len(df[cols]))
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO
    cols=df.keys()[-1]
    tv=df[cols].unique()
    av=df[attribute].unique()
    avg_info=0
    for i in av:
        entropy=0
        for j in tv:
            entropy+= -len(df[attribute][df[attribute] == i][df[cols]== j])/len(df[attribute][df[attribute]== i]) * np.log2(len(df[attribute][df[attribute] == i][df[cols]== j])/len(df[attribute][df[attribute]== i]) + 0.000001)
        avg_info+= (len(df[attribute][df[attribute]== i])/len(df))*entropy
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO
    u=np.unique(df[attribute])
    information_gain=get_entropy_of_dataset(df)
    for i in u:
        sd=df[df[attribute]==i]
        se=get_entropy_of_dataset(sd)
        information_gain += -(len(sd))/(len(df))*se
    return information_gain




#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO
    info_gain=dict()
    find=list()
    for key in df.keys()[:-1]:
        info_gain[key]=get_entropy_of_dataset(df)-get_avg_info_of_attribute(df,key)
    maxk=max(info_gain,key=lambda x:info_gain[x])
    find.append(info_gain)
    find.append(maxk)
    return tuple(find)
    pass
