class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        time = 0  # Total time 
        length = len(colors)  # Length of the 'colors' string

        # Iterate through the 'colors' string starting from the second element
        for index in range(1, length):
            # Check if the current color is the same as the previous color
            if colors[index] == colors[index - 1]:
                # Increment total time by the minimum time between current and previous color
                time += min(neededTime[index], neededTime[index - 1])
                
                # Set time needed for current color to the maximum time between current and previous color
                neededTime[index] = max(neededTime[index], neededTime[index - 1])
            
        return time  # Return the total time/cost



