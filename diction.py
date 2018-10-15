def get_stems(word):
    return [word[:i] for i in range(1, len(word))]


def get_stems_for_word_list(wl):
    stems = []
    for word in wl:    
        stems_for_word = get_stems(word)
        stems += stems_for_word
    return set(stems)



# def get_stems(word): 
   
#     index=[word[:l] for l in range(1, len(word))]
#     return index


   

# def get_stems(word):
#     count =[]
#     i=1
#     while i < len(word):
#         count.append(word[:i])
#         i+=1
#         return count

print(get_stems("HIPOPOTAMUS"))
    
# def get_stems(word): With a for loop
   
#     index=[word[:l] for l in range(1, len(word))]
#     return index
    
# print(get_stems("hello"))


    
    
    

# print(get_stems("HELLO"))