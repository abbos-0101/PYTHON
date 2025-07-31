
#1
df=df.groupby('Category').agg({'Quantity':['sum','max'],"Price":'mean'})

#1.2
product_sales = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()


top_products = product_sales.sort_values(['Category', 'Quantity'], ascending=[True, False]) \
                            .drop_duplicates(subset='Category', keep='first')

print(top_products)

1.3
df['TotalSales'] = df['Quantity'] * df['Price']

# 2. Sanaga qarab jami savdoni hisoblash
daily_sales = df.groupby('Date')['TotalSales'].sum().reset_index()

# 3. Eng yuqori savdo bo‘lgan sanani topish
max_sales_date = daily_sales.loc[daily_sales['TotalSales'].idxmax()]


# Step 1: Group by CustomerID and count the number of orders
order_counts = customer.groupby('CustomerID').size()

# Step 2: Filter CustomerIDs with 20 or more orders
valid_customers = order_counts[order_counts >= 20].index

# Step 3: Filter the original DataFrame
filtered_df = customer[customer['CustomerID'].isin(valid_customers)]

# Display the result
print(filtered_df)


# Har bir CustomerID bo‘yicha o‘rtacha narxni hisoblash
avg_price = customer.groupby('CustomerID')['Price'].mean().reset_index()

# $120 dan katta bo‘lganlarni tanlash
high_spenders = avg_price[avg_price['Price'] > 120]

# Asl jadvaldan faqat shu mijozlarga tegishli buyurtmalarni olish
filtered_data = customer[customer['CustomerID'].isin(high_spenders['CustomerID'])]

print(filtered_data)


product_summary = customer.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', lambda x: (x * customer.loc[x.index, 'Quantity']).sum())
).reset_index()

# 5 donadan kam sotilgan mahsulotlarni filtrdan o‘tkazish
filtered_products = product_summary[product_summary['total_quantity'] >= 5]

print(filtered_products)



import pandas as pd
import sqlite3

# --- STEP 1: Fayllarni yuklash ---
# 1.1 Excel fayldan salary band toifalarini yuklash
salary_band_df = pd.read_excel("C:\\Users\\user\\Downloads\\population_salary_analysis.xlsx")

# 1.2 SQLite dan population jadvalini o‘qish
conn = sqlite3.connect("C:\\Users\\user\\Downloads\\population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)

# --- STEP 2: Salary Band ni aniqlash ---
def assign_salary_band(salary):
    for _, row in salary_band_df.iterrows():
        if row['Min Salary'] <= salary <= row['Max Salary']:
            return row['Band']
    return 'Unknown'

population_df['Salary Band'] = population_df['salary'].apply(assign_salary_band)

# --- STEP 3: Umumiy statistikalar ---
total_population = len(population_df)

salary_band_stats = population_df.groupby('Salary Band').agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

salary_band_stats['Percentage'] = (salary_band_stats['Population_Count'] / total_population * 100).round(2)

# --- STEP 4: Har bir shtat bo‘yicha statistikalar ---
state_salary_stats = population_df.groupby(['State', 'Salary Band']).agg(
    Population_Count=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

# Ulushini hisoblash uchun har bir State bo‘yicha umumiy sonni topamiz
state_total = population_df.groupby('State')['Salary'].count().reset_index(name='State_Total')

# Qo‘shamiz
state_salary_stats = state_salary_stats.merge(state_total, on='State')
state_salary_stats['Percentage'] = (state_salary_stats['Population_Count'] / state_salary_stats['State_Total'] * 100).round(2)

# Faqat kerakli ustunlar
state_salary_stats = state_salary_stats[['State', 'Salary Band', 'Population_Count', 'Average_Salary', 'Median_Salary', 'Percentage']]

# --- STEP 5: Natijalarni ko‘rsatish ---
print("== Salary Band Statistics (Overall) ==")
print(salary_band_stats)

print("\n== Salary Band Statistics per State ==")
print(state_salary_stats)


import sqlite3
import pandas as pd

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('chinook.db')

# Invoice va Customer jadvallarini o'qib olish
df_invoice = pd.read_sql("SELECT CustomerId, Total FROM Invoices", conn)
df_customer = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", conn)

# Har bir mijoz bo‘yicha jami xarajatni hisoblash
df_total = df_invoice.groupby("CustomerId")["Total"].sum().reset_index()

# Mijoz ismlari bilan birlashtirish
df_total = df_total.merge(df_customer, on="CustomerId")

# Yangi ustun: To‘liq ism
df_total["FullName"] = df_total["FirstName"] + " " + df_total["LastName"]

# Ustunlarni tartibga solish
df_total = df_total[["CustomerId", "FullName", "Total"]]

# Natijani ko‘rsatish
print(df_total.head())



#2

df_invoice = pd.read_sql("SELECT CustomerId, Total FROM Invoices", connection)
df_customer = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", connection)


df_total = df_invoices.groupby("CustomerId")["Total"].sum().reset_index()

df_total = df_total.merge(df_customer, on="CustomerId")

df_total["FullName"] = df_total["FirstName"] + " " + df_total["LastName"]

# Yuqoridan pastga saralash va eng yuqori 5 ta mijozni olish
top5 = df_total.sort_values(by="Total", ascending=False).head(5)

# Natijani tanlab ko‘rsatish
print(top5[["CustomerId", "FullName", "Total"]])


#3

import sqlite3
import pandas as pd

# Baza bilan bog'lanish
conn = sqlite3.connect('chinook.db')

# Jadval ma'lumotlarini olish
df_invoice = pd.read_sql("SELECT CustomerId, Total FROM Invoices", conn)
df_customer = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customers", conn)

# Har bir mijoz bo'yicha jami sarflangan summa
df_total = df_invoice.groupby("CustomerId")["Total"].sum().reset_index()

# Mijoz ma'lumotlarini qo‘shish
df_total = df_total.merge(df_customer, on="CustomerId")

# To‘liq ism ustunini yaratish
df_total["FullName"] = df_total["FirstName"] + " " + df_total["LastName"]

# Saralash va faqat top 5 ni olish
top5 = df_total.sort_values(by="Total", ascending=False).head(5)

# Tanlangan ustunlarni ko‘rsatish
print(top5[["CustomerId", "FullName", "Total"]])



import sqlite3
import pandas as pd

# Bazaga ulanish
conn = sqlite3.connect('chinook.db')

# Jadval ma'lumotlarini olish
invoice_df = pd.read_sql("SELECT InvoiceId, CustomerId FROM Invoices", conn)
invoiceline_df = pd.read_sql("SELECT InvoiceId, TrackId FROM Invoice_items", conn)
track_df = pd.read_sql("SELECT TrackId, AlbumId FROM Tracks", conn)
customer_df = pd.read_sql("SELECT CustomerId FROM Customers", conn)

# Har bir albomda nechta trek borligini aniqlash
album_track_counts = track_df.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracksInAlbum"}, inplace=True)

# InvoiceLine + Track = qaysi InvoiceId da qaysi albomdan trek sotib olingan
invoice_tracks = invoiceline_df.merge(track_df, on="TrackId")

# Har bir invoice va album uchun nechta trek sotib olingan?
invoice_album_track_counts = (
    invoice_tracks.groupby(["InvoiceId", "AlbumId"])["TrackId"]
    .count()
    .reset_index()
    .rename(columns={"TrackId": "TracksPurchased"})
)

# Albomdagi umumiy trek sonini qo‘shish
invoice_album_full = invoice_album_track_counts.merge(album_track_counts, on="AlbumId")

# Full album sotib olinganmi? (agar barcha treklar sotib olingan bo‘lsa)
invoice_album_full["IsFullAlbum"] = invoice_album_full["TracksPurchased"] == invoice_album_full["TotalTracksInAlbum"]

# Har bir invoice bo‘yicha — hech bo‘lmasa 1 ta full album olganlar
invoice_full_album = invoice_album_full.groupby("InvoiceId")["IsFullAlbum"].any().reset_index()

# InvoiceId -> CustomerId bilan birlashtirish
invoice_full_album = invoice_full_album.merge(invoice_df, on="InvoiceId")

# Endi, har bir Customer uchun: u biron marta full album olganmi?
customer_album_pref = invoice_full_album.groupby("CustomerId")["IsFullAlbum"].any().reset_index()
