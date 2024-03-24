import streamlit as st
import pandas as pd

def read_data_from_csv(filename):
    try:
        data = pd.read_csv(filename)
        print("CSV file successfully loaded.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None



def main():
    st.title('Scraped Data Viewer')

    # Read data from CSV
    data_from_scraped_data_csv = read_data_from_csv('Project/scraped_data.csv')
    
    # Log data type and structure
    print("Type of data:", type(data_from_scraped_data_csv))
    print("Data structure:", data_from_scraped_data_csv)

    # Display the top 10 data entries in a table
    st.write('## Top 10 Data Entries')
    if isinstance(data_from_scraped_data_csv, pd.DataFrame):
        st.table(data_from_scraped_data_csv.head(10))
    else:
        st.error("Failed to load data from CSV file. Please check the data structure.")


if __name__ == '__main__':
    main()
