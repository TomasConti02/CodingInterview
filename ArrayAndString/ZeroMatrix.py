class ZeroMatrix:
    def __init__(self, data):
        self.data = data
        self.h = len(data)
        self.w = len(data[0]) if self.h > 0 else 0

    def print(self):
        """Stampa la matrice ben allineata in colonne."""
        print(f"\nDimensioni: {self.h}x{self.w}")
        for row in self.data:
            # {:>3} allinea i numeri a destra occupando 3 spazi
            print(" ".join(f"{item:>3}" for item in row))

    def draw_h(self, h):
        for w in range(self.w):
            self.data[h][w] = 0

    def draw_w(self, w):
        for h in range(self.h):
            self.data[h][w] = 0

    def set_to_zero(self):
        if not self.data or self.h == 0:
            return
        
        # because we are going to use first row and column to track 
        first_row_has_zero = any(self.data[0][w] == 0 for w in range(self.w))
        first_col_has_zero = any(self.data[h][0] == 0 for h in range(self.h))
        print(first_row_has_zero)
        print(first_col_has_zero)

        #  O(N * M)
        for h in range(1, self.h):
            for w in range(1, self.w):
                if self.data[h][w] == 0:
                    self.data[h][0] = 0  
                    self.data[0][w] = 0  

        
        for h in range(1, self.h):
            if self.data[h][0] == 0:
                self.draw_h(h)
                
        for w in range(1, self.w):
            if self.data[0][w] == 0:
                self.draw_w(w)

        # if into the first phase there was items into the first row/column draw their
        if first_row_has_zero:
            self.draw_h(0)
        if first_col_has_zero:
            self.draw_w(0)
                

if __name__ == "__main__":
    # Matrice di test 5x5 con uno zero in alto a sinistra (0,0)
    matrix = [
        [0,  2,  0,  4,  5],
        [2,  3,  3,  8,  9],
        [1,  2,  4, 11, 12],
        [13, 4, 15, 0, 17],
        [18, 19, 20, 21, 3]
    ]
    
    x = ZeroMatrix(matrix)
    
    print("--- Matrice Originale ---")
    x.print()
    
    x.set_to_zero()
    
    print("\n--- Matrice Dopo set_to_zero ---")
    x.print()