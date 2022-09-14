# ----------- Imports ----------- 


from encodings import search_function
import requests
import json
import sqlite3

from os.path import exists


# ----------- Variables and Constants -----------


hn_data_file = 'hn_search.txt'
hn_query = 'http://hn.algolia.com/api/v1/search?query=ask hn: who is hiring who\'s hiring&tags=story&numericFilters=created_at_i>1573160133&hitsPerPage=100'
search_keywords = ['location', 'postiion', 'keywords', 'remote', 'interns', 'visa', 'candidate', 'hiring', 'job']


# ----------- Function Defintions ----------- 


def get_information(search_results_p):
    '''Returns a list of dicts containing the extracted attributes from the post data'''

    list_of_results = []
    extracted_results = {}

    for post in search_results_p['hits']:
        extracted_results['created_at'] = post['created_at']
        extracted_results['title'] = post['title']
        extracted_results['objectID'] = post['objectID']
        extracted_results['story_text'] = post['story_text']
        extracted_results['num_comments'] = post['num_comments']
        
        list_of_results.append(extracted_results)
        extracted_results = {}
    
    return list_of_results


def filter_posts(search_results_p):
    '''Takes in an unfiltered list and checks if specific keywords exist in the post, then returns a filtered list'''
    
    filtered_list = []

    for post in search_results_p:
        
        found_keywords = 0
        search_string = post['story_text'].lower()
        search_string_list = search_string.split()
        
        for keyword in search_keywords:
            if keyword in search_string_list:
                found_keywords += 1
                #print(f'Keyword: {keyword}\nCount: {found_keywords}')
            if found_keywords > (len(search_keywords)/2):
                found_keywords = 0
                filtered_list.append(post)
    
    return filtered_list

# ----------- Database ----------- 


'''conn = sqlite3.connect('hn.db')
cur = conn.cursor()'''


def create_table(create_table_string):
    pass




# ----------- Main ----------- 


#Make API call if file doesnt exist
if not exists(hn_data_file):
    
    r = requests.get(hn_query)

    pretty_r = json.loads(r.text)

    search_results = json.dumps(pretty_r, indent=2)

    with open('hn_search.txt', 'w') as f:
        f.write(search_results)
else:
    print('got here trying')

with open('hn_search.txt', 'r') as f:
    data = f.read()
    search_results = json.loads(data)

id_list = get_information(search_results)

print(id_list)
'''filtered_id_list = filter_posts(id_list)

for post in filtered_id_list:
    print(post['title'])

for post in id_list:
    print(post['title'])

conn.close()'''

