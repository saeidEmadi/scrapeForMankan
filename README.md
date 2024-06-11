# scrape For Mankan
This is a student project for a data mining course and is a simple exercise
In this project, we have tried to extract data from a site using ``` web scraping ``` and ``` crawling ``` methods and create a data set.
And after cleaning and preparing the data set, we first analyze it and then use the obtained results to predict and guide users.

*You can easily calculate the amount of calories needed based on the amount of daily activity :*
  - **ridingBike**
  - **running**
  - **walking**
  - **cleaningUp**
    
*and foods that provide the same amount of calories to the body.*


## DataSet ![Mankan_dataset.csv](https://github.com/saeidEmadi/scrapeForMankan/blob/main/Mankan_dataset.csv)
This dataset contains useful information such as the amount of ```calories, protein, etc```. about foods and edibles

**This dataset has 1821 records and 11 columns**

| siteId | name | calory | carbo | protein | fat | fiber | activity1 | activity2 | activity3 | activity4 |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |

The unit of columns is as :
- ` siteId ` : *Integer*
- ` name ` : *String*
- ` calory ` : *Kcal[kilocalorie]*
- ` carbo ` : *g[Gram]*
- ` protein ` : *g[Gram]*
- ` fat ` : *g[Gram]*
- ` fiber ` : *g[Gram]*
- `activity1 = ridingBike` : *m[Minute]*
- `activity2 = running` : *m[Minute]*
- `activity3 = walking` : *m[Minute]*
- `activity4 = cleaningUp` : *m[Minute]*


In this project, we use the following two models with the specified accuracy:
- `Linear regression`: *0.84*
- `RandomForestRegressor`: *0.87*
  
we have used **RandomForestRegressor** for prediction because is very accurate.



**Dataset Reference :** ![Mankan.me](https://www.mankan.me/)
> [!TIP]
> Thanks to the Mankan site
