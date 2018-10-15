from string import ascii_uppercase
from random import choice

def make_grid(columns, rows):
    return {(c,r): choice(ascii_uppercase) 
                    for r in range(rows) 
                        for c in range(columns) }
    
def potential_neighbours(position):
    c, r = position #position is a tuple. This position gives you the neighbors(8) of that position
    return [(c-1, r-1), (c, r-1),  (c+1, r-1), #This is the list of 8 neighbours
            (c-1, r),               (c+1, r), 
            (c-1, r+1), (c, r+1),  (c+1, r+1)]
            
def path_to_word(path,grid): #each psotition matches a letter
    word = ""
    for position in path:
        word += grid[position]
        return word

def load_word_list(filename):#If the word is found then it will split it
    with open (filename) as f:
        text= f.read().upper().split("\n")
    
    return text
    
def get_real_neighbours(grid): #Not all the position has 8 neighbours. Go through each psotion in the grid, find the potencial neighbours (8)
                               #and then just return the ones that that position has on the grid. it descarts those positions
    real_neighbours = {}        # that aren't neighbours
    
    for position in grid:
        pn= potential_neighbours(position)
        on_the_grid =[p for p in pn if p in grid]
        
        # for p in pn:
        #     if p in grid:
        #         on_the_grid.append(p)
        real_neighbours[position] = on_the_grid
        
    return real_neighbours
    
def search(grid, dictionary):
    neighbours = get_real_neighbours(grid)
    paths = []
    
    def do_search(path):
        word = path_to_word(path, grid)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
        words = []
    
    for path in paths:
        words.append(path_to_word(path, grid))
    return set(words)
    
    
def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))

def main():
    grid = make_grid(3, 3)
    word_list = load_word_list("words.txt")
    print(word_list)
    words = search(grid, word_list)
    display_words(words)
    
main()    

    



# words = load_word_list("words.txt")
# if "ZINC" in words:
#     print ("Yes")
# else:
#     print("No")


# text = load_word_list("words.txt")
# print(len(text)

# print(load_word_list("words.txt"))
# mygrid= make_grid(2,2)
# path=[(1,1),(0,1),(0,0)]

# path_to_word(path,mygrid)