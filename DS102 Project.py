import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

carbon_emissions_df= pd.read_csv("vehicle population.csv")
carbon_emissions_df

emissions_copy_df= carbon_emissions_df.copy()
car_type_gb= emissions_copy_df.groupby("car_type")
Grouped_car_type=car_type_gb['number'].size().reset_index()

Grouped_car_type
#Upon closer inspection, the data for 'car_type' has some labels mislabelled. 
#Data-cleaning is needed.

#Cleaning data for column 'car_type'
replaced=emissions_copy_df['car_type'].replace('Cars and Station-wagons','Cars & Station-wagons')
emissions_copy_df['car_type']=replaced.apply(np.str)

replaced2=emissions_copy_df['car_type'].replace('Goods and Other Vehicles','Goods & Other Vehicles')
emissions_copy_df['car_type']=replaced2.apply(np.str)

replaced3=emissions_copy_df['car_type'].replace('Motorcycles and Scooters','Motorcycles')
emissions_copy_df['car_type']=replaced3.apply(np.str)

car_type_gb= emissions_copy_df.groupby("car_type")
Grouped_car_type=car_type_gb['number'].size().reset_index()
Grouped_car_type

#Cleaned data for car_type is ensured

car_type2_gb= emissions_copy_df.groupby("car_type2")
Grouped_car_type2=car_type2_gb['number'].size().reset_index()
Grouped_car_type2

#Upon closer inspection, the data for 'car_type2' has some labels mislabelled. 
#Data-cleaning is needed.


emissions_copy_df[emissions_copy_df['car_type']=='Tax Exempted Vehicles']
#As seen below, for car_type2, there is mislabelling of Motorcycles, 
#Motorcycles and scooters


emissions_copy_df[(emissions_copy_df['car_type2']=='Motorcycles and Scooters')|(emissions_copy_df['car_type2']=='Motorcycles and scooters')]

replaced_type2=emissions_copy_df['car_type2'].replace('Cars and Station-wagons','Cars & Station-wagons')
emissions_copy_df['car_type2']=replaced_type2.apply(np.str)

replaced_type2i=emissions_copy_df['car_type2'].replace('Goods and Other Vehicles','Goods & Other Vehicles')
emissions_copy_df['car_type2']=replaced_type2i.apply(np.str)

replaced_type2ii=emissions_copy_df['car_type2'].replace('Motorcycles','Motorcycles and Scooters')
emissions_copy_df['car_type2']=replaced_type2ii.apply(np.str)

replaced_type2iii=emissions_copy_df['car_type2'].replace('Motorcycles and scooters','Motorcycles and Scooters')
emissions_copy_df['car_type2']=replaced_type2iii.apply(np.str)



car_type2_gb= emissions_copy_df.groupby("car_type2")
Grouped_car_type2=car_type2_gb['number'].size().reset_index()
Grouped_car_type2

#i)Group all vehicles based on year reflecting their carbon emissions
#ii)Group each car_type with number contrast with year
#iii)Group each car_type2 with number contrast with year

#change to x(each car type(1&2)) to year with number and total counted


#Part i) Grouping Carbon Emissions of all vehicles based on year 

year_gb= emissions_copy_df.groupby('year')
year_gb_df=year_gb['number'].sum().reset_index(name='Carbon Emissions of all Vehicles')
year_gb_df.head()


fig=plt.figure(figsize=(8,7))
ax1=fig.add_subplot(111)

year_gb_df.plot(kind='line',
               x='year',
               y='Carbon Emissions of all Vehicles',
               figsize=(16,8),
               marker='o',
               alpha=0.9,
               color='dodgerblue',
               ax=ax1)

plt.ylabel('Carbon Emissions,a.u')
plt.title('Total Carbon Emissions of all Vehicles from 2005 to 2017')
plt.legend(['Carbon Emissions'])

plt.show()

#This shows that there is a general increase of carbon emissions of all vehicles from about 760000 a.u to about 
#960000 a.u in 2017. Hence my hypothesis is true.


#Part ii) Group each car_type with number contrast with year

car_type_gb= emissions_copy_df.groupby(["car_type","year"])
Grouped_car_type_df=car_type_gb['number'].sum().reset_index(name='Emissions of car_type across year')
Grouped_car_type_df.head()


transpose_car_type_1_df=Grouped_car_type_df.transpose()
a=transpose_car_type_1_df.transpose()
a.head()


df_final=pd.pivot_table(a,
                        index = "year", 
                        columns= 'car_type', 
                        values= 'Emissions of car_type across year',
                        aggfunc= np.sum).reset_index()
df_final.head()


fig = plt.figure(figsize=(25, 30))

ax1 = fig.add_subplot(4,2,1)
ax2 = fig.add_subplot(4,2,2)
ax3 = fig.add_subplot(4,2,3)
ax4 = fig.add_subplot(4,2,4)
ax5 = fig.add_subplot(4,2,5)
ax6 = fig.add_subplot(4,2,6)
ax7 = fig.add_subplot(4,1,4)

df_final.plot(kind='bar',
              x='year', 
              y='Buses', 
              ax=ax1,
              color="tomato")

ax1.set_ylabel("Carbon Emission,a.u")
ax1.set_title("Carbon Emissions of Buses from 2005 to 2017")
ax1.set_yticks(np.arange(0, 650000, 50000)) #This needs to be specified so both charts are on the same scale.

df_final.plot(kind='bar',
              x='year', 
              y='Cars & Station-wagons', 
              ax=ax2,
              color="aqua")

ax2.set_ylabel("Carbon Emission,a.u")
ax2.set_title("Carbon Emissions of Cars & Station-wagons from 2005 to 2017")
ax2.set_yticks(np.arange(0, 650000, 50000))

df_final.plot(kind='bar',
              x='year', 
              y='Goods & Other Vehicles', 
              ax=ax3,
              color="navy")

ax3.set_ylabel("Carbon Emission,a.u")
ax3.set_title("Carbon Emissions of Goods & Other Vehicles from 2005 to 2017")
ax3.set_yticks(np.arange(0, 650000, 50000))
 

df_final.plot(kind='bar',
              x='year', 
              y='Motorcycles', 
              ax=ax4,
              color="green")

ax4.set_ylabel("Carbon Emission,a.u")
ax4.set_title("Carbon Emissions of Motorcycles from 2005 to 2017")
ax4.set_yticks(np.arange(0, 650000, 50000))

df_final.plot(kind='bar',
              x='year', 
              y='Taxis', 
              ax=ax5,
              color="gold")

ax5.set_ylabel("Carbon Emission,a.u")
ax5.set_title("Carbon Emissions of Taxis from 2005 to 2017")
ax5.set_yticks(np.arange(0, 650000, 50000))

df_final.plot(kind='bar',
              x='year', 
              y='Tax Exempted Vehicles', 
              ax=ax6,
              color="magenta")

ax6.set_ylabel("Carbon Emission,a.u")
ax6.set_title("Carbon Emissions of Tax Exempted Vehicles from 2005 to 2017")
ax6.set_yticks(np.arange(0, 650000, 50000))

df_final.plot(kind='bar', 
              x='year',
              stacked=True, 
              title="No. of Loans by Grade",
              ax=ax7)

plt.suptitle("Carbon Emissions of car_type across from 2005-2017", fontsize=30)
plt.show()

#Hence it shows that "Cars & Station-wagons" contribute the most in terms of percentage(based on comparing sizes of bar
#charts) and hence my hypothesis is true.

#As the bar chart above is limited in showing the other percentage as stated in my hypothesis. Further Data 
#manipulation and visulisation is required

Grouped_car_type2

car_type2_gb= emissions_copy_df.groupby(["car_type2","year"])
Grouped_car_type2_df=car_type2_gb['number'].sum().reset_index(name='Emissions of car_type2 across year')
Grouped_car_type2_df.head(20)


df_final2=pd.pivot_table(Grouped_car_type2_df,
                         index = "year",
                         columns= 'car_type2', 
                         values= 'Emissions of car_type2 across year',
                         aggfunc= np.sum).reset_index()
df_final2

#Group 1(6): Buses, Excursion Buses, Omnibuses, Private Buses, Private Hire Buses, School Buses(CB)
#Group 2(7): Car & Station-wagons, Company cars, off peak cars, Private cars, Rental Cars, Taxis, Tuition Cars
#Group 3(5): Goods & Other Vehicles, Goods-cum-passenger vehicles (GPVs),Heavy Goods Vehicles (HGVs),
#Light Goods Vehicles (LGVs),Very Heavy Goods Vehicles (VHGVs)
#Group 4(1): Motorcycles and Scooters


fig,ax1= plt.subplots(figsize=(8,6))


sns.lineplot(x=df_final2['year'], 
             y=df_final2['Cars & Station-wagons'],
             color='r',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Company cars'], 
             color='b',
             ax=ax1)    

sns.lineplot(x=df_final2['year'], 
             y=df_final2['Off peak cars'], 
             color='y',
             ax=ax1) 
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Private cars'],
             color='g',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Rental cars'], 
             color='k',
             ax=ax1)    
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Taxis'], 
             color='c',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Tuition cars'], 
             color='tan',
             ax=ax1)


ax1.set(ylabel='Carbon Emissions of Cars from 2005 to 2017,a.u')
ax1.legend(['Cars & Station-wagons', 'Company cars', 'off peak cars', 'Private cars', 'Rental Cars', 'Taxis', 
            'Tuition Cars'], facecolor='w')
plt.show()


fig,ax1= plt.subplots(figsize=(8,6))


sns.lineplot(x=df_final2['year'], 
             y=df_final2['Buses'],
             color='r',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Excursion buses'], 
             color='b',
             ax=ax1)    

sns.lineplot(x=df_final2['year'], 
             y=df_final2['Omnibuses'], 
             color='y',
             ax=ax1) 
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Private buses'],
             color='g',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Private hire buses'], 
             color='k',
             ax=ax1)    
sns.lineplot(x=df_final2['year'], 
             y=df_final2['School buses (CB)'], 
             color='m',
             ax=ax1)
ax1.set(ylabel='Carbon Emissions of Buses from 2005 to 2017,a.u')
ax1.legend(['Buses', 'Excursion buses','Omnibuses','Private buses','Private hire buses','School buses (CB)'], facecolor='w')
plt.show()

fig,ax1= plt.subplots(figsize=(8,6))


sns.lineplot(x=df_final2['year'], 
             y=df_final2['Goods & Other Vehicles'],
             color='r',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Goods-cum-passenger vehicles (GPVs)'], 
             color='b',
             ax=ax1)    

sns.lineplot(x=df_final2['year'], 
             y=df_final2['Heavy Goods Vehicles (HGVs)'], 
             color='y',
             ax=ax1) 
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Light Goods Vehicles (LGVs)'],
             color='g',
             ax=ax1)
sns.lineplot(x=df_final2['year'], 
             y=df_final2['Very Heavy Goods Vehicles (VHGVs)'], 
             color='k',
             ax=ax1)    

ax1.set(ylabel='Carbon Emissions of Goods Carrying Vehicles from 2005 to 2017,a.u')
ax1.legend(['Goods & Other Vehicles', 'Goods-cum-passenger vehicles (GPVs)','Heavy Goods Vehicles (HGVs)',
            'Light Goods Vehicles (LGVs)','Very Heavy Goods Vehicles (VHGVs)'], facecolor='w')
plt.show()


fig,ax1= plt.subplots(figsize=(8,6))


sns.lineplot(x=df_final2['year'], 
             y=df_final2['Motorcycles and Scooters'],
             color='r',
             ax=ax1)


ax1.set(ylabel='Carbon Emissions of Motorcyles and Scooters from 2005 to 2017,a.u')
ax1.legend(['Motorcycles and Scooters'], facecolor='w')
plt.show()


#From the 4 graphs.

#With regards to Hypothesis 2, (from the 1st graph) "Private Cars" have a significantly greater number of carbon
#emissions compared to the rest of the car types. This ties in with hypothesis 2 for car_type2

#With regards to Hypothesis 3, (from the 3rd Graph) "School Buses(CB)" has a significantly lower number of carbon
#emissions compared to the rest of the buses but it is not the lowest(Lowest is "Buses"). This ties in largely with
#my hypothesis 3 for car_type2

fig.savefig("Bar Chart showing Carbon Emssions of car_type.png")


cartype2_change_df=df_final.copy()
cartype2_change_df[['Buses',
                    'Cars & Station-wagons',
                    'Goods & Other Vehicles',
                    'Motorcycles',
                    'Tax Exempted Vehicles',
                    'Taxis']]=cartype2_change_df[['Buses',
                                        'Cars & Station-wagons',
                                        'Goods & Other Vehicles',
                                        'Motorcycles',
                                        'Tax Exempted Vehicles',
                                        'Taxis']].pct_change(periods=1)
cartype2_change_df.head()


fig = plt.figure(figsize=(20, 25))

ax1 = fig.add_subplot(4,2,1)
ax2 = fig.add_subplot(4,2,2)
ax3 = fig.add_subplot(4,2,3)
ax4 = fig.add_subplot(4,2,4)
ax5 = fig.add_subplot(4,2,5)
ax6 = fig.add_subplot(4,2,6)

cartype2_change_df.plot(kind='line',
                        x='year',
                        y='Buses',
                        marker="x",
                        alpha=0.9,
                       color='tomato',
                       ax=ax1)


ax1.set_ylabel("Percentage Change,%")
ax1.set_title("Year-on-Year Percentage Change of Carbon Emissions of Buses")
ax1.set_yticks(np.arange(-0.2, 0.2, 0.05))

cartype2_change_df.plot(kind='line',
                        x='year',
                        y='Cars & Station-wagons',
                        marker="x",
                        alpha=0.9,
                       color='aqua',
                       ax=ax2)

ax2.set_ylabel("Percentage Change,%")
ax2.set_title("Year-on-Year Percentage Change of Carbon Emissions of Cars & Station-wagons")
ax2.set_yticks(np.arange(-0.2, 0.2, 0.05))


cartype2_change_df.plot(kind='line',
                        x='year',
                        y='Goods & Other Vehicles',
                        marker="x",
                        alpha=0.9,
                       color='navy',
                       ax=ax3)

ax3.set_ylabel("Percentage Change,%")
ax3.set_title("Year-on-Year Percentage Change of Carbon Emissions of Goods & Other Vehicles")
ax3.set_yticks(np.arange(-0.2, 0.2, 0.05))

cartype2_change_df.plot(kind='line',
                        x='year',
                        y='Motorcycles',
                        marker="x",
                        alpha=0.9,
                       color='green',
                       ax=ax4)

ax4.set_ylabel("Percentage Change,%")
ax4.set_title("Year-on-Year Percentage Change of Carbon Emissions of Motorcycles")
ax4.set_yticks(np.arange(-0.2, 0.2, 0.05))

cartype2_change_df.plot(kind='line',
                        x='year',
                        y='Tax Exempted Vehicles',
                        marker="x",
                        alpha=0.9,
                       color='gold',
                       ax=ax5)

ax5.set_ylabel("Percentage Change,%")
ax5.set_title("Year-on-Year Percentage Change of Carbon Emissions of Tax Exempted Vehicles")
ax5.set_yticks(np.arange(-0.2, 0.2, 0.05))

cartype2_change_df.plot(kind='line',
                        x='year',
                        y='Taxis',
                        marker="x",
                        alpha=0.9,
                       color='magenta',
                       ax=ax6)

ax6.set_ylabel("Percentage Change,%")
ax6.set_title("Year-on-Year Percentage Change of Carbon Emissions of Taxi")
ax6.set_yticks(np.arange(-0.2, 0.2, 0.05))

#With regards to Hypothesis 2),the highest increase in percentage of carbon emissions year on year is actually 
#"Tax Exempted Vehicles" instead of "Car and Station-Wagons". The graph of 
#"Carbon Emissions of Cars & Station-wagons from 2005 to 2017" is always positive and the highest postive percentage
#change(>0.02)

#With regards to Hypothesis 3),the lowest increase in percentage is "Taxi" instead of "Buses" as the percentage change 
#is mostly in negative region. This shows that from 2005 to 2017, the carbon emissions of Taxi's is generally 
#decreasing

#Hypothesis 1 : There is a general increase of carbon emissions(Number) for all types of vehicles(car_type and 
#car_type2) from 2005 to 2017.

#Hypothesis 2: Car & Station-wagons(Private Cars) contribute the most carbon emissions
#in terms of percentage of all type of vehicles(car_type 2) and had the greatest increase 
#of carbon emission in terms of percentage from 2005 to 2017.

#Hypothesis 3: Buses(School Buses(CB)) contribute the least carbon emissions
#in terms of percentage of all type of vehicles(car_type 2) and had the lowest increase 
#of carbon emission in terms of percentage from 2005 to 2017.


#In conclusion,

#As per results from data cleaning, exploratory data analysis(Data Visualisation).
#Hypothesis 1 is true.
#Hypothesis 2 is true but the greatest increse in percentage of carbon emissions is actually "Tax Exempted Vehicles".
#Hypothesis 3 is true to a small extent. Buses(car_type) contribute to the lowest carbon emissions amongst all the
#vehicles but for car_type2 within buses (Buses contributed) the least instead. Also, "Taxi" had the lowest increase 
#of percentage of carbon emissions instead of "Buses"











