"""Tender loving functions."""





def love(subject: str) -> str:
   """Given a subject  as a paramenter, returns a loving string"""
   return f"I love you {subject}"

print(love("kris"))


def spread_love(to: str, n: int) ->str: 
    """Generates a str repeating a locing message n times"""
    love_note: str = ""
    i: int = 0 
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note
