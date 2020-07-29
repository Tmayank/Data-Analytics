# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:47:49 2020

@author: mayan
"""


from absenteeism_module import*

model = absenteeism_model('model' , 'scaler')
model.load_and_clean_data('Absenteeism_new_data.csv')
model.predicted_outputs()

import pymysql

conn = pymysql.connect(database = 'predicted_outputs' , user = 'root' , password = '365Pass' )
cursor = conn.cursor()

df_new_obs = model.predicted_outputs()
cursor.execute('Select * from predicted_outputs;')
insert_query = 'INSERT into predicted_outputs Values'
# print(str(df_new_obs.shape[1][6]))
for i in range(df_new_obs.shape[0]) :
    insert_query += '('
for j in range(df_new_obs.shape[1]) :
             insert_query += str(df_new_obs[df_new_obs.columns.values[j]][i]) + ','
             insert_query = insert_query[:-2] + '),'
             
             insert_query = insert_query[:-2] + ';'

             
             
cursor.execute(insert_query)
cursor.commit()
cursor.close()
         

