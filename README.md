# Python-Projects
List of python projects that I have explored or collabrated with others

# DS102.py

# Summary
Developed a project "Study of carbon emissions of different types of vehicle population from 2005 to 2014 in Singapore" analyzing data gathered from csv excel file from Kaggle depicting the carbon emissions for different vehicles in Singapore. employed data cleaning skills using Pandas library and data visualization tools from matplotlib library.

# Data Cleaning  

In data cleaning, there is removal of mislabeled categories (different spelling, wrong word use) and followed by grouping of general vehicles types (i.e buses, car & station-wagons,…) based on carbon emissions produced by year. 

Uncleaned data for label "car_type"
![mislabeled categories](https://github.com/JiaJun98/Python-Projects/blob/master/Data_Cleaning_car_type1.PNG)
Cleaned data for label "car_type"
![mislabeled categories](https://github.com/JiaJun98/Python-Projects/blob/master/Cleaned%20data%20for%20car_type.PNG)
Uncleaned data for label "car_type2"
![mislabeled categories](https://github.com/JiaJun98/Python-Projects/blob/master/Data_Cleaning_car_type2.PNG)
Cleaned data for label "car_type2"
![mislabeled categories](https://github.com/JiaJun98/Python-Projects/blob/master/Cleaned%20data%20for%20car_type2.PNG)



This grouping concluded that there is a general increase of carbon emissions of all vehicles from about 760000 arbitrary units (a.u) to about 960000 arbitrary units (a.u) in 2017. 
![general increase](https://github.com/JiaJun98/Python-Projects/blob/master/Total_Carbon_Emissions_of_all_Vehicles_from_2005_to_2017(Line).PNG)

The second grouping was grouping specific vehicle type (i.e school buses, tuition cars, private cars,…)based on carbon emissions produced by year. 

Inspecting the size of bar charts from matplotlib library, “Cars & station-wagons” contributed the most in terms of percentage compared to the rest of the general vehicle types(as seen from the orange region stacked bar-chart at the last row)
![car_type increase](https://github.com/JiaJun98/Python-Projects/blob/master/Carbon_Emissions_of_car_types_(2005-2017).png)

However, the the bar charts were limited in showing the individual percentage of the specific vehicle types, further data manipulation and visualization is required.

# Data Visualisation

Using data visualization techniques from Matplotlib library, line graphs were used to compare the magnitude of carbon emissions of specific vehicle types (i.e excursion buses, omnibuses, private buses) across specific vehicle types (i.e buses).

The graph shows that for car types, “Private cars” have a significant greater number of carbon emissions.

![car_type increase](https://github.com/JiaJun98/Python-Projects/blob/master/Carbon%20Emissions%20of%20Cars%20from%202005%20to%202017%2Ca.u.png)

Whereas for the bus types, “School buses” have a significantly lower number of carbon emissions.
![car_type increase](https://github.com/JiaJun98/Python-Projects/blob/master/Carbon%20Emissions%20of%20Buses%20from%202005%20to%202017%2Ca.u.png)

Upon further analysis of year-on-year percentage change of carbon emissions for general vehicle types (i.e buses, car & station-wagons,…). 
Insights gathered showed that the greatest increase in year-on-year percentage change of carbon emissions is “Tax exempted vehicles"(represented by the yellow line graph).

Whereas, the lowest year-on-year percentage change of carbon emissions is "Taxi" as the percentage change is mostly in negative region(represented by the purple line graph). This shows that from 2005 to 2017, the carbon emissions of taxi's are generally decreasing.

![year_on_year increase](https://github.com/JiaJun98/Python-Projects/blob/master/Year-on-Year%20Percentage%20Change%20each%20type%20of%20Vehicles.png)

# Conclusion

In conclusion, my project showed 3 results
1)	There is a general increase of carbon emissions for all types of vehicles from 2005 to 2017.
2)	“Car & Station-wagon” vehicle contributed the most carbon emissions in terms of percentage of all specific vehicle type but “Tax exempted vehicles" had the greatest increase of carbon emission in terms of percentage from 2005 to 2017.
3)	The greatest year-on-year percentage change of carbon emissions for general vehicle types was “Tax exempted vehicles” while the lowest greatest year-on-year percentage change was “Taxi”.

