class Solution:
    def findContentChildren(self, greed, cookies) -> int:
        # sort two lists
        greed.sort()
        cookies.sort()
        
        # Initialize two pointers
        number_children = 0
        cookie_index = 0
        
        for g in greed:
            # Find the smallest cookie that can satisfy the current child
            while cookie_index < len(cookies) and cookies[cookie_index] < g:
                cookie_index += 1
            
            # If a suitable cookie is found, assign it to the child
            if cookie_index < len(cookies):
                number_children += 1
                cookie_index += 1  # Move to the next cookie
        
        return number_children   