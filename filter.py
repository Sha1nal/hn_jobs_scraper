import re

search_keywords = ['location', 'postiion', 'keywords', 'remote', 'interns', 'visa', 'candidate', 'hiring', 'job']
month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'deccember']
year_list = ['2019', '2020', '2021', '2022']
month_string = "january|february|march|april|may|june|july|august|september|october|november|deccember"
year_string = "2019|2020|2021|2022"

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
    


    def filter_posts(self):
        '''Takes in an unfiltered list and checks if specific keywords exist in the post, then returns a filtered list'''
    
        filtered_list = []

        for post in self.list_of_results:
            title = post['title'].lower()
            
            test_exp = re.search("^ask hn: who is hiring?", title)
            month_check = re.findall(month_string, title)
            year_check = re.findall(year_string, title)

            if test_exp and month_check and year_check:
                filtered_list.append(post)
            
        return filtered_list
        
        