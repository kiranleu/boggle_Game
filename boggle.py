from string import ascii_uppercase
from random import choice

def make_grid(columns, rows):
    return { (c,r) : choice(ascii_uppercase) 
                        for r in range(rows) 
                            for c in range(columns) }

def potential_neighbours(position):
    c, r = position
    return [(c-1, r-1), (c, r-1),  (c+1, r-1), 
            (c-1, r),              (c+1, r), 
            (c-1, r+1), (c, r+1),  (c+1, r+1)]
    

def path_to_word(path, grid):
    word = ""
    for position in path:
        word += grid[position]
    return word


def load_word_list(filename):
    with open(filename) as f:
        text = f.read().upper().split("\n")
        
    return set(text)
    

def get_real_neighbours(grid):
    real_neighbours = {}
    
    for position in grid:
        pn = potential_neighbours(position)
        on_the_grid = [p for p in pn if p in grid]
        real_neighbours[position] = on_the_grid
    
    return real_neighbours
    


def get_real_neighbours_of_a_position(position, grid):
    pn = potential_neighbours(position)
    return [ p for p in pn if p in grid]


def is_a_real_word(word, dictionary):
    return word in dictionary
    
    
def get_stems(word):
    return [word[:i] for i in range(1, len(word))]


def get_stems_for_word_list(wl):
    stems = []
    for word in wl:    
        stems_for_word = get_stems(word)
        stems += stems_for_word
    return set(stems)


def search(grid, dictionary):
    neighbours = get_real_neighbours(grid)
    stems = get_stems_for_word_list(dictionary)
    words = []
    
    def do_search(path):
        word = path_to_word(path, grid)
        if is_a_real_word(word, dictionary):
            words.append(word)
            
        if word in stems:
            for next_pos in neighbours[path[-1]]:
                if next_pos not in path:
                    do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
        
   
   
    return set(words)


def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))

def main():
    grid = make_grid(500, 500)
    word_list = load_word_list("words.txt")
    words = search(grid, word_list)
    display_words(words)

main()    
    
    