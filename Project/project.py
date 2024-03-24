import streamlit as st
import pandas as pd

def read_data_from_csv(filename, encoding='utf-8'):
    try:
        data = pd.read_csv(filename, encoding=encoding, error_bad_lines=False)
        return data
    except Exception as e:
        st.error(f"Error reading CSV file: {e}")

def search(keyword, data):
    filtered_data = data[data.apply(lambda row: keyword.lower() in str(row).lower(), axis=1)]
    return filtered_data

def main():
    st.title('Data Search App')

    data_from_scraped_data_csv = read_data_from_csv('Project/scraped_data.csv')

    if data_from_scraped_data_csv is not None:
        st.write("## Data")
        st.write(data_from_scraped_data_csv.head(10))

        st.write("## Search")

        keyword = st.text_input("Enter keyword:")
        if st.button("Search"):
            filtered_data = search(keyword, data_from_scraped_data_csv)
            if filtered_data.empty:
                st.write("No results found.")
            else:
                st.write(filtered_data)

if __name__ == "__main__":
    main()
