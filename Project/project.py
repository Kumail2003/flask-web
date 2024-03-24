import streamlit as st
import csv

def read_data_from_csv(filename):
    data = []
    with open(filename, 'r', newline='', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def search(keyword):
    data_from_scraped_data_csv = read_data_from_csv('Project/scraped_data.csv')
    filtered_data = [row for row in data_from_scraped_data_csv if any(keyword.lower() in str(value).lower() for value in row.values())]
    return filtered_data

def main():
    st.title('Scraped Data')

    # Display scraped data
    st.header('Scraped Data')
    data_from_scraped_data_csv = read_data_from_csv('Project/scraped_data.csv')
    for i, row in enumerate(data_from_scraped_data_csv[:10]):
        st.write(f'{i+1}. {row}')

    # Search functionality
    st.header('Search Data')
    keyword = st.text_input('Enter Keyword')
    if st.button('Search'):
        search_results = search(keyword)
        if search_results:
            st.write('Search Results:')
            for result in search_results:
                st.write(result)
        else:
            st.write('No results found.')

if __name__ == '__main__':
    main()
