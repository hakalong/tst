import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
path1 = '/ap1/wangzh01/python/data/'

lsting = pd.read_csv(path1+'listings.csv',dtype = object)
tbed = pd.read_csv(path1+'ZipZhvi2bedroom .csv')

nyzip = pd.read_csv(path1+'nyzip.csv',header =None)
nyzip.columns = ['zip','name']
nyzip_lst  =  [v for v in nyzip['zip']]
snyzip_lst =  [str(v) for v in nyzip['zip']]

#slim_list
sls = lsting[lsting['zipcode'].isin(snyzip_lst)]
useful_var1 = ['id','name','neighbourhood_cleansed','street','city','state','zipcode',
               'property_type','room_type','bedrooms','beds','bed_type',
               'price','weekly_price','monthly_price','security_deposit']
sls = sls[useful_var1].fillna('')
#del lsting

#slim_tbed
stb = tbed[tbed['RegionName'].isin(nyzip_lst)]
#del tbed

# for var in ['price','weekly_price','monthly_price']:
#     print([type(v) for v in sls[var]])
#[v for v in sls['price']]

# for var in ['price','weekly_price','monthly_price']:
#     sls[var] = [float(v[1:].replace(',','')) if len(v) >0 else v for v in sls[var] ]

#sls['price'] = [float(v[1:].replace(',','')) for v in sls['price']]
#sls['weekly_price'] = [float(v[1:].replace(',','')) for v in sls['weekly_price']]
#sls['monthly_price'] = [float(v[1:].replace(',','')) for v in sls['monthly_price']]
#float('1,2300.00'.replace(',',''))

sls2 = sls[sls['bedrooms'] == '2']

print(sls2.shape)
print(sls.shape)

sls2.groupby(['room_type','zipcode']).describe()[['price']]

#stb.head()
#sstb = stb.drop(['RegionID','City','State','Metro','CountyName','SizeRank'],axis = 1)
#sls.loc[:,['id','has_availability','availability_30','availability_60','availability_90','availability_365','number_of_reviews','review_scores_rating']]

#stb.describe().loc[:,stb.describe().loc['count'] >0]
#stb[stb['RegionID'].isin([62044,61790,62120,61782,61788])]
# #sns.distplot(list(stb.loc[0,'2005-04':]))
# plt.figure(figsize=(8,6),dpi = 80)
# #for i in stb[stb['RegionID'].isin([61780,61781,61785,61784,61779])].index:
# for i in stb.index:
#     print(i)
#     plt.plot(stb.loc[i,'1996-04':])
# plt.show()
