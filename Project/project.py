import streamlit as st
import csv

def read_data_from_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def main():
    st.title('Data Viewer')

    # Read data from CSV
    data_from_scraped_data_csv = read_data_from_csv('scraped_data.csv')

    # Display the data
    st.write('## Top 10 Data Entries')
    enumerated_data = [(i + 1, row) for i, row in enumerate(data_from_scraped_data_csv[:10])]
    for index, row in enumerated_data:
        st.write(f"### Entry {index}")
        st.write(row)

    # Search functionality
    st.sidebar.title("Search")
    keyword = st.sidebar.text_input("Enter keyword:")
    if keyword:
        filtered_data = [row for row in data_from_scraped_data_csv if any(keyword.lower() in str(value).lower() for value in row.values())]
        if filtered_data:
            st.write('## Search Results')
            for row in filtered_data:
                st.write(row)
        else:
            st.write("No results found for the given keyword.")

if __name__ == '__main__':
    main()
