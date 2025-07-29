#1
import pandas as pd

# 1. creationdate ustunini datetime formatga o'tkazish
df["creationdate"] = pd.to_datetime(df["creationdate"], errors='coerce')

# 2. Yil ajratish
df["year"] = df["creationdate"].dt.year

# 3. 2014-yildan keyingi ma'lumotlar
filt = df["creationdate"] > pd.to_datetime("2014-01-01")

# 4. Natijani chiqarish
df_filtered = df[filt]
df_filtered


#2

filt=df['score']>50

df[filt]


#3

filt=df['score'].between(50,100)

df[filt]


#4

filt=df['ans_name']=='Scott Boston'

df[filt]


#5
target_users = ['Mike Pennington', 'doug', 'Demitri', 'Max', 'Lennart Regebro']
filtered_questions = df[df['ans_name'].isin(target_users)][['id', 'title', 'ans_name']]
print(filtered_questions)



#6
import pandas as pd

# 1. To'g'ri datetime aylantirish
df["creationdate"] = pd.to_datetime(df["creationdate"], errors='coerce')

# 2. Yil va oy ajratish
df["year"] = df["creationdate"].dt.year
df["month"] = df["creationdate"].dt.month

# 3. Sana oralig'ida filtr (Martdan Oktabrgacha 2014)
filt = df["creationdate"].between("2014-03-01", "2014-10-31")



filt1=df['score']<5
filt2=df['ans_name']=='unutbu'

final_filt= filt & filt1 & filt2

df[final_filt]



#7

filt1=df['score'].between(5,10)
filt2=df['viewcount']>10000

final_filt= filt1 & filt2

df.loc[final_filt,['id','score','viewcount']]


#8

filt=df['ans_name'] != 'Scott Boston'

df[filt]


#1
t1=titanic['Pclass'] == 1
t2=titanic['Age'].between(20,30)

t_final= t1 & t2

titanic[t_final]

#2
t=titanic['Fare']>100

titanic[t]


#3
t1=titanic['Survived'] == 0
t2=titanic['SibSp'] == 1

t_final= t1 & t2

titanic[t_final]



#4

t1=titanic['Embarked'] == 'C'
t2=titanic['Fare'] > 50

t_final= t1 & t2

titanic[t_final]


#5
t1=titanic['SibSp'] > 0
t2=titanic['Parch'] > 0

t_final= t1 & t2

titanic[t_final]



#6
t1=titanic['Age'] <= 15
t2=titanic['Survived'] == 1

t_final= t1 & t2

titanic[t_final]


#7

t1=titanic['Cabin'].notna()
t2=titanic['Fare'] > 200

t_final= t1 & t2

titanic[t_final]


#8
t=titanic["PassengerId"] % 2 == 1
titanic[t]


#9
t=titanic["Ticket"].value_counts()

t1= t[t == 1].index

unique_ticket_passengers = titanic[titanic['Ticket'].isin(t1)]


print(unique_ticket_passengers)

#10
t = titanic[
    titanic['Name'].str.contains('Miss') &
    (titanic['Sex'] == 'female') &
    (titanic['Pclass'] == 1)
]

print(t)
