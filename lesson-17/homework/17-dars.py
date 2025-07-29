data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)


#1.1
df.rename(columns={'First Name': 'first_name','Age':'age'}, inplace=True)
print(df)


#1.2

print(df.head(3))

#1.3 mean age
i=df['age'].mean()

print(i)


#1.4

l=df[['first_name','City']]

print(l)


#1.5
import numpy as np
df['Salary']=np.random.randint(50000,100001,size=len(df))
df


#1.6
print(df.describe())


#2.1
sales_and_expences = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 
         'Sales': [5000, 6000, 7500, 8000], 
         'Expences': [3000,3500,4000,4500]} 
sl = pd.DataFrame(sales_and_expences)




#2.2

s1=sl[['Sales','Expences']].max()

print("Maximum:",s1)


#2.3

s2=sl[['Sales','Expences']].min()

print("Minimum:",s2)


s3=sl[['Sales','Expences']].mean()

print("Average:",s3)


expences = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'], 
         'January': [1200, 200, 300, 150], 
         'February': [1300,220,320,160],
         'March': [1400,240,330,170],
         'April': [1500,250,350,180]} 
ex = pd.DataFrame(expences)


ex['Max_Expense'] = ex[['January', 'February', 'March', 'April']].max(axis=1)

# Display result
print(ex[['Category', 'Max_Expense']])



ex['Max_Expense'] = ex[['January', 'February', 'March', 'April']].min(axis=1)

# Display result
print(ex[['Category', 'Max_Expense']])


ex['Max_Expense'] = ex[['January', 'February', 'March', 'April']].mean(axis=1)

# Display result
print(ex[['Category', 'Max_Expense']])

ex.set_index('Category')
