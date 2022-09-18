"""An exampl of a list utility algorithm."""

# Name: contains
# function with two parameters:
# needle -- what  we"re searching for
# haystack - what we're searching through
# Return Type: bool
def contains(needle: str, haystack: list[str]) -> bool:
    # Start from first index
    i: int = 0 
    # loop through each index of list
    while i < len(haystack):
        #   Test is equal to needle
        if haystack[i] == needle:
        #       # Yes! Return True
            return True 
        i += 1
    # Return False
    return False 