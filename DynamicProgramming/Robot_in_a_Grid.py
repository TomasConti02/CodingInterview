# 1. Define Grid Dimensions and "Off-Limits" Cells (False = Blocked)
"""
grid = [
    [True,  True,  True,  True],
    [True,  False, True,  True],  # (1, 1) is blocked
    [False, True,  False, True],  # (2, 0) and (2, 2) are blocked
    [True,  True,  True,  True]
]
"""
grid = [
    [True,  True,  True,  True],
    [True,  False, True,  True],  # (1, 1) is blocked
    [True, True,  False, True],  # (2, 0) and (2, 2) are blocked
    [True,  True,  False,  True]
]
ROWS = len(grid)
COLS = len(grid[0])

def get_path(grid):

    if not grid or len(grid) == 0:
        return None
    
    path = set() 
    path_cache = set() 
    COUNT=0
    if get_path_helper(grid, 0, 0, path, path_cache, COUNT):
        print(f"cache: {path_cache}")
        return path
    
    return None

def get_path_helper(grid, r, c, path, path_cache, COUNT):

    if r >= ROWS or c >= COLS:
        return False
    
    if grid[r][c]==False:
        print(f" NOPE {COUNT} ----> {(r, c)}")
        COUNT+=1
        return False

    if (r, c) in path_cache:
        print(f" BLOCK {COUNT} ----> {(r, c)}")
        COUNT+=1
        return False

    if c==3 and r == 3:
        print(f" FIND OUT {COUNT} ----> {(r, c)}")
        COUNT+=1
        return True
    
    
    path.add((r, c))
    print(f"{COUNT} ----> {(r, c)}")
    COUNT+=1

    buttom=get_path_helper(grid, r, c+1, path, path_cache, COUNT)
    right=None
    if buttom is False:
        right=get_path_helper(grid, r+1, c, path, path_cache, COUNT)
    
    if buttom is False:
        path_cache.add(  (r, c)  )

    if right is False:
        path_cache.add(  (r, c)  )

    if right or buttom:

        return True
    else:
        return False

"""
def get_path_helper(grid, r, c, path, path_cache, COUNT):

    #if (r, c) in path_cache:
        #return False
    
    if r >= ROWS or c >= COLS: #borderf [0, 3] 

        return "barrier"

    if grid[r][c]==False:
        
        return False #it is not the right paths
    
    if c==3 and r == 3:
        print(f"found -> {(r, c) } ----- count {COUNT}")
        COUNT+=1
        path.add((r, c))

        return True
    
    
    right_path=get_path_helper(grid, r+1, c, path, path_cache, COUNT)
    if right_path == False:
        path_cache.add( (r, c))
    
    buttom_path=get_path_helper(grid, r, c+1, path, path_cache, COUNT)
    if buttom_path == False:
        path_cache.add( (r, c))

    ###### maybe devo fare cache dei path gia trovati oppure va bene cosi ###########
    if right_path ==True and buttom_path==True:
        print("\n branch \n")
    if right_path ==False and buttom_path==False:

        return False
    
    if right_path ==True or buttom_path==True:
        print(f" {(r, c)} -------- count {COUNT}" )
        COUNT+=1
        path.add( (r, c) )
        return True
    
"""


# --- NUOVA FUNZIONE PER STAMPARE LA MATRICE ---
def print_grid(grid, path=None):
    """
    Stampa la griglia in modo leggibile.
    Se viene passato un percorso (path), mostra i passaggi all'interno della griglia.
    """
    path_set = set(path) if path else set()
    
    print("\n--- VISUALIZZAZIONE GRIGLIA ---")
    for r in range(len(grid)):
        row_str = []
        for c in range(len(grid[0])):
            if (r, c) == (0, 0):
                row_str.append(" S ") # Start (Inizio)
            elif (r, c) == (len(grid)-1, len(grid[0])-1) and (r, c) in path_set:
                row_str.append(" E ") # End (Fine) raggiunto
            elif (r, c) in path_set:
                row_str.append(" * ") # Cella che fa parte del percorso
            elif not grid[r][c]:
                row_str.append(" █ ") # Ostacolo / Cella bloccata
            else:
                row_str.append(" * ") # Cella libera vuota
        print("".join(row_str))
    print("-------------------------------\n")


# --- Run the Template ---
if __name__ == "__main__":
    print(f"grid shape: {ROWS}, {COLS}")
    result_path = get_path(grid)
    print(f"Path trovato (coordinate): {result_path}")
    print_grid(grid, path=result_path)

"""
if r < 0 or c < 0 or not grid[r][c]:
        return False
    
    if (r, c) in failed_cells:
        return False
    
    is_at_origin = (r == 0 and c == 0)
    
    if is_at_origin or get_path_helper(grid, r - 1, c, path, failed_cells) or get_path_helper(grid, r, c - 1, path, failed_cells):
        path.append((r, c))
        return True
    
    failed_cells.add((r, c))
    return False
"""