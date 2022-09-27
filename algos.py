# Class of quick and dirty self implemented algorithims 

def bubble_sort(filtered_list_p):
    
    filtered_list = filtered_list_p

    tracker = 0

    while len(filtered_list) - tracker > 0:
        comparing_element = 0
        testing_element = 1

        while comparing_element < len(filtered_list) - tracker - 1:
            if filtered_list[comparing_element]['objectID'] >= filtered_list[testing_element]['objectID']:
                #swap elements
                middle_obj = filtered_list[comparing_element]
                filtered_list[comparing_element] = filtered_list[testing_element]
                filtered_list[testing_element] = middle_obj

            comparing_element += 1
            testing_element += 1    
               

        tracker += 1

    return filtered_list