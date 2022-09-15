search_keywords = ['location', 'postiion', 'keywords', 'remote', 'interns', 'visa', 'candidate', 'hiring', 'job']
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'deccember']
year_list = ['2019', '2020', '2021', '2022']

class Filter():
    
    def __init__(self, search_results_p):
        self.search_results = search_results_p
        self.list_of_results = []
        self.get_information()
        


    def get_information(self):
        '''Returns a list of dicts containing the extracted attributes from the post data'''

        extracted_results = {}

        for post in self.search_results['hits']:
            extracted_results['created_at'] = post['created_at']
            extracted_results['title'] = post['title']
            extracted_results['objectID'] = post['objectID']
            extracted_results['story_text'] = post['story_text']
            extracted_results['num_comments'] = post['num_comments']
            extracted_results['created_at_i'] = post['created_at_i']
            
            self.list_of_results.append(extracted_results)
            extracted_results = {}
    


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