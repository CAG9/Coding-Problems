class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        index_sum = 1000000
        restaurant_name = {}
        
        for restaurant in list1:
            #check if have similar rest
            if restaurant in list2:
                #check the index
                restaurant_name[restaurant] = list1.index(restaurant) + list2.index(restaurant)  
                
        min_value =  min(restaurant_name.items(), key=lambda x: x[1])[1] 
        
        result = []
        for restaurant in restaurant_name:
            if restaurant_name[restaurant] == min_value:
                 result.append(restaurant)
        
        
        return result         
