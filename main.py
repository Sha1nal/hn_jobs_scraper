# ----------- Imports ----------- 

import requests
import json
import filter
import algos


from os.path import exists


# ----------- Variables and Constants -----------


hn_data_file = 'hn_search.txt'
hn_query = 'http://hn.algolia.com/api/v1/search?query=ask hn: who is hiring who\'s hiring&tags=story&numericFilters=created_at_i>1573160133&hitsPerPage=100'


# ----------- Function Defintions ----------- 


# ----------- Main ----------- 


#Make API call if file doesnt exist
if not exists(hn_data_file):
    
    r = requests.get(hn_query)

    pretty_r = json.loads(r.text)

    search_results = json.dumps(pretty_r, indent=2)

    with open('hn_search.txt', 'w') as f:
        f.write(search_results)

with open('hn_search.txt', 'r') as f:
    data = f.read()
    search_results = json.loads(data)


result_list = filter.Filter(search_results)

filtered_list = result_list.filter_posts()
sorted_list = algos.bubble_sort(filtered_list)

i = 0
for result in sorted_list:
    post_id = result['objectID']
    title = result['title']
    text = result['story_text']
    date = result['created_at']

    print(f"ID: {post_id}\nTitle: {title}\nText: {text}\nDate: {date}\n")




