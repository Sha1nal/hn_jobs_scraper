# ----------- Imports ----------- 


from encodings import search_function
import requests
import json
import sqlite3
import filter

from os.path import exists


# ----------- Variables and Constants -----------


hn_data_file = 'hn_search.txt'
hn_query = 'http://hn.algolia.com/api/v1/search?query=ask hn: who is hiring who\'s hiring&tags=story&numericFilters=created_at_i>1573160133&hitsPerPage=100'


# ----------- Function Defintions ----------- 


# ----------- Database ----------- 


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


result_list = filter.Filter(search_results)

for result in result_list.list_of_results:
    print(f"{result['title']} - {result['created_at_i']}")
