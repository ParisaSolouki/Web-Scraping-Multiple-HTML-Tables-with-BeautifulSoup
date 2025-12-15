#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Multiple HTML Tables with BeautifulSoup
# 
# This notebook scrapes structured data from an HTML page that contains:
# 1. Tourism statistics (city, country, visitors)
# 2. Wikipedia reference links
# 3. City images
# 
# We then clean the numeric column and merge everything into a single final DataFrame.
# 

# In[14]:


from bs4 import BeautifulSoup
import pandas as pd


# In[15]:


# Raw HTML (simulated web page)
html_data = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Top Tourist Cities</title>
</head>
<body>

<h2>Most Visited Cities</h2>
<table class="tourism-stats">
  <tr>
    <th>City</th>
    <th>Country</th>
    <th>Visitors (Millions)</th>
  </tr>
  <tr>
    <td>Paris</td>
    <td>France</td>
    <td>19.1</td>
  </tr>
  <tr>
    <td>Bangkok</td>
    <td>Thailand</td>
    <td>22.8</td>
  </tr>
  <tr>
    <td>Dubai</td>
    <td>UAE</td>
    <td>16.7</td>
  </tr>
</table>

<h2>City References</h2>
<table class="city-references">
  <tr>
    <th>City</th>
    <th>Wikipedia</th>
  </tr>
  <tr>
    <td>Paris</td>
    <td><a href="https://en.wikipedia.org/wiki/Paris">Link</a></td>
  </tr>
  <tr>
    <td>Bangkok</td>
    <td><a href="https://en.wikipedia.org/wiki/Bangkok">Link</a></td>
  </tr>
  <tr>
    <td>Dubai</td>
    <td><a href="https://en.wikipedia.org/wiki/Dubai">Link</a></td>
  </tr>
</table>

<h2>City Images</h2>
<table class="city-images">
  <tr>
    <th>City</th>
    <th>Image</th>
  </tr>
  <tr>
    <td>Paris</td>
    <td><img src="/images/paris.jpg" alt="Paris"></td>
  </tr>
  <tr>
    <td>Bangkok</td>
    <td><img src="/images/bangkok.jpg" alt="Bangkok"></td>
  </tr>
  <tr>
    <td>Dubai</td>
    <td><img src="/images/dubai.jpg" alt="Dubai"></td>
  </tr>
</table>

</body>
</html>"""


# In[16]:


# Parse HTML
soup = BeautifulSoup(html_data, "html.parser")


# In[20]:


# Step 1: Extract tourism table
tourism_table = soup.find("table", class_="tourism-stats")
rows = tourism_table.find_all("tr")

cities = []
countries = []
visitors = []

for row in rows[1:]:  # skip header
    cols = row.find_all("td")
    if len(cols) >= 3:
        city = cols[0].text.strip()
        country = cols[1].text.strip()
        visitor = cols[2].text.strip()

        cities.append(city)
        countries.append(country)
        visitors.append(visitor)

tourism_df = pd.DataFrame({
    "City": cities,
    "Country": countries,
    "Visitors (Millions)": visitors
})

tourism_df


# In[18]:


tourism_df.dtypes


# In[21]:


# Step 2: Clean visitors column (convert to numeric)
tourism_df["Visitors (Millions)"] = (
    tourism_df["Visitors (Millions)"]
    .str.replace(",", "", regex=False)
    .pipe(pd.to_numeric, errors="coerce")
)

tourism_df.dtypes


# In[24]:


# Step 3: Extract Wikipedia links table
reference_table = soup.find("table", class_="city-references")
rows = reference_table.find_all("tr")

ref_cities = []
wiki_urls = []

for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 2:
        city = cols[0].text.strip()
        a_tag = cols[1].find("a")
        url = a_tag.get("href") if a_tag else None

        ref_cities.append(city)
        wiki_urls.append(url)

references_df = pd.DataFrame({
    "City": ref_cities,
    "Wikipedia_URL": wiki_urls
})


references_df


# In[25]:


# Step 4: Extract images table (src -> absolute URL)
image_table = soup.find("table", class_="city-images")
rows = image_table.find_all("tr")

img_cities = []
img_urls = []


for row in rows[1:]:
    cols = row.find_all("td")
    if len(cols) >= 2:
        city = cols[0].text.strip()
        img_tag = cols[1].find("img")
        src = img_tag.get("src") if img_tag else None


        img_cities.append(city)
        img_urls.append(src)

images_df = pd.DataFrame({
    "City": img_cities,
    "Image_URL": img_urls
})

images_df


# In[27]:


# Make relative URLs absolute
base_url = "https://example.com"  # replace with real domain if needed

images_df["Image_URL"] = images_df["Image_URL"].apply(
    lambda x: base_url + x if x.startswith("/") else x
)

images_df


# In[34]:


# Step 5: Merge all DataFrames into one final dataset
final_df = tourism_df.merge(references_df, on="City", how="left")
final_df = final_df.merge(images_df, on="City", how="left")

final_df


# In[30]:


# Step 6: Export
final_df.to_csv("final_city_data.csv", index=False)
print("Saved: final_city_data.csv")

