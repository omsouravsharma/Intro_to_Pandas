# Introduction to Pandas
# Import pandas
import pandas as pd
# Series is 1-dimensional

series = pd.Series(['BMW', 'Toyota', 'Honda'])
colors = pd.Series(['Red', 'Blue', 'White'])

print(series)
print(colors)

# DataFrame = 2-Dimensional

car_data = pd.DataFrame({
    'Car make': series,
    'Color': colors
})

print(car_data)

# Importing car-sales data; pd.read_csv function
car_sales = pd.read_csv('car-sales.csv')

print(car_sales) # Printing car sales data

# Exporting to csv file
car_sales.to_csv('exported-car-sakes.csv', index=False)

# Describe Data
# Attribute
print("------Attribute---------")
print(car_sales.dtypes)

print(car_sales.columns)
print(car_sales.index)

print("--Functions--")
print(car_sales.describe()) # work only on numeric

print(car_sales.info())

# print(car_sales.mean())

print(car_sales.sum())

print(car_sales["Doors"].sum())

print(f"Length {len(car_sales)}")