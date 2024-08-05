import pandas as pd
students={
'Name':['santhi','kumari','lavanya','rahulchoudari'],
'ID':[101,102,103,104],
'Class':['A','B','C','D'],
'Branch':['ece','cse','eee','civil'],
'Hostal Room':['A101','B102','C103','D104'],
'Contact':['123-456-7890','1234-456-678','7890-9876-45','799-5608-244'],
'Remarks':['Good student','excllent','need improvment','super']
}
df=pd.DataFrame(students)
print(df)
