# import libraries
import pandas as pd
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

# Import datasets from csv
control_data = pd.read_csv("control_group.csv", sep = ";")
test_data = pd.read_csv("test_group.csv", sep = ";")

# Align column names between datasets
control_data.columns = ["Campaign Name", "Date", "Amount Spent",
                        "Number of Impressions", "Reach", "Website Clicks",
                        "Searches Received", "Content Viewed", "Added to Cart",
                        "Purchases"]

test_data.columns = ["Campaign Name", "Date", "Amount Spent",
                     "Number of Impressions", "Reach", "Website Clicks",
                     "Searches Received", "Content Viewed", "Added to Cart",
                     "Purchases"]

# # Find number of null values in dataset
# print(control_data.isnull().sum())
# print(test_data.isnull().sum())

# Fill missing values of control_data with average
control_data["Number of Impressions"].fillna(value=control_data["Number of Impressions"].mean(), inplace=True)
control_data["Reach"].fillna(value=control_data["Reach"].mean(), inplace=True)
control_data["Website Clicks"].fillna(value=control_data["Website Clicks"].mean(), inplace=True)
control_data["Searches Received"].fillna(value=control_data["Searches Received"].mean(), inplace=True)
control_data["Content Viewed"].fillna(value=control_data["Content Viewed"].mean(), inplace=True)
control_data["Added to Cart"].fillna(value=control_data["Added to Cart"].mean(), inplace=True)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(), inplace=True)

# Merge control dataset and test dataset
ab_data = control_data.merge(test_data, how="outer").sort_values(["Date"])
ab_data = ab_data.reset_index(drop=True)

# Plot relationship between 'Number of Impressions' and 'Amount Spent'
figure = px.scatter(data_frame=ab_data,
                    x="Number of Impressions",
                    y="Amount Spent",
                    size="Amount Spent",
                    color="Campaign Name",
                    color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"},
                    trendline="ols"
                    )
figure.write_html('output_file_name.html', auto_open=True)

# Plot relationship between 'Content Viewed' and 'Number of Website Clicks' and
figure = px.scatter(data_frame=ab_data,
                    x="Content Viewed",
                    y="Website Clicks",
                    size="Website Clicks",
                    color="Campaign Name",
                    color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"},
                    trendline="ols"
                    )
figure.write_html('output_file_name.html', auto_open=True)

# Plot relationship between 'Number of Products Added to Cart' and 'Content Viewed'
figure = px.scatter(data_frame=ab_data,
                    x="Added to Cart",
                    y="Content Viewed",
                    size="Added to Cart",
                    color="Campaign Name",
                    color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"},
                    trendline="ols"
                    )
figure.write_html('output_file_name.html', auto_open=True)

# Plot relationship between 'Number of Purchases' and 'Number of items Added to Cart'
figure = px.scatter(data_frame=ab_data,
                    x="Purchases",
                    y="Added to Cart",
                    size="Purchases",
                    color="Campaign Name",
                    color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"},
                    trendline="ols"
                    )
figure.write_html('output_file_name.html', auto_open=True)

# Look at number of Searches
label = ["Total Searches - Control",
         "Total Searches - Test"]
counts = [sum(control_data["Searches Received"]),
          sum(test_data["Searches Received"])]
colors = ['lightblue', 'lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Control Vs Test: Searches')
fig.update_traces(hoverinfo='label+percent',
                  textinfo='value',
                  textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black',width=3))
                  )
figure.write_html('output_file_name.html', auto_open=True)

# Look at number of Website Clicks
figure = px.histogram(data_frame=ab_data,
                      x="Campaign Name",
                      y="Website Clicks",
                      color ="Campaign Name",
                      color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"}
                      )
figure.write_html('output_file_name.html', auto_open=True)

# Look at number of Content Views
figure = px.histogram(data_frame=ab_data,
                      x="Campaign Name",
                      y="Website Clicks",
                      color ="Campaign Name",
                      color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"}
                      )
figure.write_html('output_file_name.html', auto_open=True)

# Look at number of products Added to Cart
figure = px.histogram(data_frame=ab_data,
                      x="Campaign Name",
                      y="Added to Cart",
                      color ="Campaign Name",
                      color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"}
                      )
figure.write_html('output_file_name.html', auto_open=True)

# Look at Amount Spent
figure = px.histogram(data_frame=ab_data,
                      x="Campaign Name",
                      y="Amount Spent",
                      color ="Campaign Name",
                      color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"}
                      )
figure.write_html('output_file_name.html', auto_open=True)

# Look at Purchases
figure = px.histogram(data_frame=ab_data,
                      x="Campaign Name",
                      y="Purchases",
                      color ="Campaign Name",
                      color_discrete_map={"Control Campaign": "lightblue", "Test Campaign": "lightgreen"}
                      )
figure.write_html('output_file_name.html', auto_open=True)
