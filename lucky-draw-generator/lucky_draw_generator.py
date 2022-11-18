# -*- coding: utf-8 -*-

"""

Created on Wed Apr 20 17:25:12 2022



@author: rishi

"""

import pandas as pd

#import numpy as np

state='Bihar'

def lucky_draw_pooling(count,input_df,prize,load_limit):

    mod_input_df = input_df.loc[input_df['Load Limit']>=load_limit]

    output_df = pd.DataFrame()

    for i in range(count):

        temp_2 = mod_input_df.sample(n=1).reset_index()   #random_state=1

        output_df = output_df.append(temp_2)

        #input_df = input_df.where(Lucky_draw_bihar['CRN'] != temp_2['CRN'][0]).dropna();

        mod_input_df = mod_input_df.where(mod_input_df['Plant Name'] != temp_2['Plant Name'][0]).dropna();

        input_df = input_df.where(input_df['Plant Name'] != temp_2['Plant Name'][0]).dropna();

    output_df["Reward"]=prize

    return output_df,input_df;


def customer_filter(input_df,winners_list_df):

    
    for i in range(len(winners_list_df)):

        input_df = input_df.where(input_df['CRN'] != winners_list_df['CRN'][i]).dropna();

        #mod_input_df = mod_input_df.where(mod_input_df['Plant Name'] != temp_2['Plant Name'][0]).dropna();

        #input_df = input_df.where(input_df['Plant Name'] != temp_2['Plant Name'][0]).dropna();


    return input_df;



df_filtered_customers_list = pd.read_csv('all_customers_removed.csv')

df_winners_may = pd.read_csv('winners_may.csv')
df_winners_may = df_winners_may.loc[:,['CRN']].copy()

df_customer_modified = df_filtered_customers_list.loc[:,['Plant Name', 'CRN', 'Name','Load Limit','State','NOC']].copy()
df_customer_modified = df_customer_modified.where(df_customer_modified.State == state).dropna();



df_all_customers = pd.read_csv('all_customers.csv')
df_customer_modified_all = df_all_customers.loc[:,['Plant Name', 'CRN', 'Name','Load Limit','State','NOC']].copy()
df_customer_modified_all = df_customer_modified_all.where(df_customer_modified_all.State == state).dropna();






#Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar.NOC == 'Shahjitpur').dropna();


df_customer_modified_shpt = df_customer_modified.where(df_customer_modified.NOC == 'Shahjitpur').dropna();



Lucky_draw_list_shpt_winners= pd.DataFrame();



prize = 'TV'

count = 1

load_limit = 2000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_shpt = lucky_draw_pooling(count,df_customer_modified_shpt,prize,load_limit)

Lucky_draw_list_shpt_winners = Lucky_draw_list_shpt_winners.append(winners_list_df)







prize = 'Fridge'

count = 1

load_limit = 2000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_shpt = lucky_draw_pooling(count,df_customer_modified_shpt,prize,load_limit)

Lucky_draw_list_shpt_winners = Lucky_draw_list_shpt_winners.append(winners_list_df)





prize = 'Grinder'

count = 2

load_limit = 1000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_shpt = lucky_draw_pooling(count,df_customer_modified_shpt,prize,load_limit)

Lucky_draw_list_shpt_winners = Lucky_draw_list_shpt_winners.append(winners_list_df)







prize = 'Fan'

count = 5

load_limit = 100

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_shpt = lucky_draw_pooling(count,df_customer_modified_shpt,prize,load_limit)

Lucky_draw_list_shpt_winners = Lucky_draw_list_shpt_winners.append(winners_list_df)







# update the code


df_customer_modified_others = df_customer_modified.where(df_customer_modified.NOC != 'Shahjitpur').dropna();






Lucky_draw_list_other_winners= pd.DataFrame();



prize = 'Fridge'

count = 1

load_limit = 2000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_other_winners = Lucky_draw_list_other_winners.append(winners_list_df)







prize = 'Grinder'

count = 3

load_limit = 1000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_other_winners = Lucky_draw_list_other_winners.append(winners_list_df)






prize = 'Fan'

count = 5

load_limit = 100

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_other_winners = Lucky_draw_list_other_winners.append(winners_list_df)



Lucky_draw_list_bihar_winners= pd.DataFrame()
Lucky_draw_list_bihar_winners = Lucky_draw_list_bihar_winners.append(Lucky_draw_list_other_winners)
Lucky_draw_list_bihar_winners = Lucky_draw_list_bihar_winners.append(Lucky_draw_list_shpt_winners)
Lucky_draw_list_bihar_winners.reset_index(inplace=True,drop=True)



df_customer_modified_all_nowinners = customer_filter(df_customer_modified_all,Lucky_draw_list_bihar_winners)
df_customer_modified_all_nowinners.reset_index(inplace=True,drop=True)
df_customer_modified_all_nowinners = customer_filter(df_customer_modified_all_nowinners,df_winners_may)
df_customer_modified_all_nowinners.reset_index(inplace=True,drop=True)




df_customer_modified_all_nowinners=df_customer_modified_all_nowinners.loc[df_customer_modified_all_nowinners['Load Limit']<=1000]





prize = 'Iron'
count = 49
load_limit = 50
winners_list_df = pd.DataFrame()
winners_list_df,df_customer_modified_all_nowinners = lucky_draw_pooling(count,df_customer_modified_all_nowinners,prize,load_limit)
Lucky_draw_list_bihar_winners = Lucky_draw_list_bihar_winners.append(winners_list_df)



Lucky_draw_list_bihar_winners.to_csv('Lucky_draw_list_bihar_winners_latest.csv')




##UP Code is starting

state='Uttar Pradesh'



df_filtered_customers_list = pd.read_csv('all_customers_removed.csv')

df_winners_may = pd.read_csv('winners_may.csv')
df_winners_may = df_winners_may.loc[:,['CRN']].copy()

df_customer_modified = df_filtered_customers_list.loc[:,['Plant Name', 'CRN', 'Name','Load Limit','State','NOC']].copy()
df_customer_modified = df_customer_modified.where(df_customer_modified.State == state).dropna();



df_all_customers = pd.read_csv('all_customers.csv')
df_customer_modified_all = df_all_customers.loc[:,['Plant Name', 'CRN', 'Name','Load Limit','State','NOC']].copy()
df_customer_modified_all = df_customer_modified_all.where(df_customer_modified_all.State == state).dropna();


# update the code



df_customer_modified_others = df_customer_modified.copy()





Lucky_draw_list_up_winners= pd.DataFrame();



prize = 'TV'

count = 1

load_limit = 2000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_up_winners = Lucky_draw_list_up_winners.append(winners_list_df)


prize = 'Fridge'

count = 2

load_limit = 2000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_up_winners = Lucky_draw_list_up_winners.append(winners_list_df)





prize = 'Grinder'

count = 5

load_limit = 1000

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_up_winners = Lucky_draw_list_up_winners.append(winners_list_df)





prize = 'Fan'

count = 10

load_limit = 100

winners_list_df = pd.DataFrame()

winners_list_df,df_customer_modified_others = lucky_draw_pooling(count,df_customer_modified_others,prize,load_limit)

Lucky_draw_list_up_winners = Lucky_draw_list_up_winners.append(winners_list_df)




Lucky_draw_list_up_winners.reset_index(inplace=True,drop=True)



df_customer_modified_all_nowinners = customer_filter(df_customer_modified_all,Lucky_draw_list_up_winners)
df_customer_modified_all_nowinners.reset_index(inplace=True,drop=True)
df_customer_modified_all_nowinners = customer_filter(df_customer_modified_all_nowinners,df_winners_may)
df_customer_modified_all_nowinners.reset_index(inplace=True,drop=True)




df_customer_modified_all_nowinners=df_customer_modified_all_nowinners.loc[df_customer_modified_all_nowinners['Load Limit']<=1000]





prize = 'Iron'
count = 74
load_limit = 50
winners_list_df = pd.DataFrame()
winners_list_df,df_customer_modified_all_nowinners = lucky_draw_pooling(count,df_customer_modified_all_nowinners,prize,load_limit)
Lucky_draw_list_up_winners = Lucky_draw_list_up_winners.append(winners_list_df)



Lucky_draw_list_up_winners.to_csv('Lucky_draw_list_up_winners_latest.csv')

Lucky_draw_list_up_winners = Lucky_draw_list_up_winners.append(Lucky_draw_list_bihar_winners)

Lucky_draw_list_up_winners.to_csv('Lucky_draw_list_june_winners_latest.csv')





















'''



















df_customer_100_above = df_customer_modified.loc[df_customer_modified['Load Limit']>=100]



Lucky_draw_bihar = pd.DataFrame()





Lucky_draw_bihar = df_customer_100_above.where(df_customer_100_above.State == 'Uttar Pradesh').dropna();





#Fourth Reward: Fan Winners of Bihar, 10 winners



Lucky_draw_list_bihar_fan = pd.DataFrame()

for i in range(10):

    temp_4 = Lucky_draw_bihar.sample(n=1,random_state=9).reset_index()  

    Lucky_draw_list_bihar_fan = Lucky_draw_list_bihar_fan.append(temp_4)

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['CRN'] != temp_4['CRN'][0]).dropna();

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['Plant Name'] != temp_4['Plant Name'][0]).dropna();

    

Lucky_draw_list_bihar_fan["Reward"]='Fan'





Lucky_draw_bihar = Lucky_draw_bihar.loc[Lucky_draw_bihar['Load Limit']>=1000]





Lucky_draw_list_bihar_grinder = pd.DataFrame()

for i in range(5):

    temp_3 = Lucky_draw_bihar.sample(n=1,random_state=2).reset_index()  

    Lucky_draw_list_bihar_grinder = Lucky_draw_list_bihar_grinder.append(temp_3)

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['CRN'] != temp_3['CRN'][0]).dropna();

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['Plant Name'] != temp_3['Plant Name'][0]).dropna();

    

Lucky_draw_list_bihar_grinder["Reward"]='Grinder'











Lucky_draw_bihar = Lucky_draw_bihar.loc[Lucky_draw_bihar['Load Limit']>=2000]













    

#Second Reward: Fridge Winners of Bihar, 2 winners



Lucky_draw_list_bihar_fridge = pd.DataFrame()

for i in range(2):

    temp_2 = Lucky_draw_bihar.sample(n=1,random_state=1).reset_index()  

    Lucky_draw_list_bihar_fridge = Lucky_draw_list_bihar_fridge.append(temp_2)

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['CRN'] != temp_2['CRN'][0]).dropna();

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['Plant Name'] != temp_2['Plant Name'][0]).dropna();

    

Lucky_draw_list_bihar_fridge["Reward"]='Fridge'





#Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar.NOC == 'Shahjitpur').dropna();

#Special condition to ensure one tv is present in Sahajitpur







Lucky_draw_list_bihar_tv = pd.DataFrame()



for i in range(1):

    temp_1 = Lucky_draw_bihar.sample(n=1,random_state=1).reset_index()  

    Lucky_draw_list_bihar_tv = Lucky_draw_list_bihar_tv.append(temp_1)

    #Lucky_draw_list_bihar_tv.insert(0, 'Reward', 'TV')

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['CRN'] != temp_1['CRN'][0]).dropna();

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['Plant Name'] != temp_1['Plant Name'][0]).dropna();

    

Lucky_draw_list_bihar_tv["Reward"]='TV'









    





#Fifth Reward: Iron Winners of Bihar, 60 winners(1 per plant)





df_customer_modified_all = df_all_customers_all.loc[:,['Plant Name','Phone Number', 'CRN', 'Name','Load Limit','State','NOC']].copy()



df_customer_100_1000 = df_customer_modified_all.loc[df_customer_modified_all['Load Limit']>=50]



df_customer_100_1000 = df_customer_100_1000 .loc[df_customer_100_1000['Load Limit']<=1000]



Lucky_draw_bihar = df_customer_100_1000.where(df_customer_100_1000.State == 'Uttar Pradesh').dropna();







Lucky_draw_list_bihar_iron = pd.DataFrame()

for i in range(74):

    temp_5 = Lucky_draw_bihar.sample(n=1,random_state=1).reset_index()  

    Lucky_draw_list_bihar_iron = Lucky_draw_list_bihar_iron.append(temp_5)

    Lucky_draw_bihar = Lucky_draw_bihar.where(Lucky_draw_bihar['Plant Name'] != temp_5['Plant Name'][0]).dropna();

        

Lucky_draw_list_bihar_iron["Reward"]='Iron'



   

    

Lucky_draw_list_bihar_winners= pd.DataFrame()

Lucky_draw_list_bihar_winners = Lucky_draw_list_bihar_winners.append(Lucky_draw_list_bihar_tv)

Lucky_draw_list_bihar_winners = Lucky_draw_list_bihar_winners.append(Lucky_draw_list_bihar_fridge)

Lucky_draw_list_bihar_winners = Lucky_draw_list_bihar_winners.append([Lucky_draw_list_bihar_grinder,Lucky_draw_list_bihar_fan,Lucky_draw_list_bihar_iron])



Lucky_draw_list_bihar_winners.reset_index(inplace=True,drop=True)                                     

#Lucky_draw_list_bihar_grinder, Lucky_draw_list_bihar_fan,Lucky_draw_list_bihar_iron], axis=0)



Lucky_draw_list_bihar_winners.to_csv('Lucky_draw_list_up_winners.csv')



    
'''


    

    

    