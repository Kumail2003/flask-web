import streamlit as st
import pandas as pd

def read_data_from_csv(filename):
    try:
        data = pd.read_csv(filename, encoding='utf-8')
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

    # Display the top 10 data entries in a table
    st.write('## Top 10 Data Entries')
    st.table(data_from_scraped_data_csv.head(10))

    # Search functionality
    st.sidebar.title("Search")
    keyword = st.sidebar.text_input("Enter keyword:")
    if keyword:
        filtered_data = data_from_scraped_data_csv[data_from_scraped_data_csv.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
        if not filtered_data.empty:
            st.write('## Search Results (Tabular Format)')
            st.table(filtered_data)

            st.write('## Search Results (JSON Format)')
            st.json(filtered_data.to_dict(orient='records'))
        else:
            st.write("No results found for the given keyword.")

if __name__ == '__main__':
    main()
