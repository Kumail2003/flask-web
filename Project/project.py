import streamlit as st
import pandas as pd

def read_data_from_csv(filename):
    return pd.read_csv(filename)

def main():
    st.title('Scraped Data Viewer')

    # Read data from CSV
    data_from_scraped_data_csv = read_data_from_csv('scraped_data.csv')

    # Display the top 10 data entries in a table
    st.write('## Top 10 Data Entries')
    st.write(data_from_scraped_data_csv.head(10))

    # Search functionality
    st.sidebar.title("Search")
    keyword = st.sidebar.text_input("Enter keyword:")
    if keyword:
        filtered_data = data_from_scraped_data_csv[data_from_scraped_data_csv.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
        if not filtered_data.empty:
            st.write('## Search Results')
            st.write(filtered_data)
        else:
            st.write("No results found for the given keyword.")

if __name__ == '__main__':
    main()
