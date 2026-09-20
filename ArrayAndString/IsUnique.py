class IsUnique:
    def __init__(self, data):
        # Convert string to list if necessary, as strings are immutable
        self.data = list(data) if isinstance(data, str) else data

    def print(self):
        print(self.data)

    def IsUnique(self, x=None, strategy="set"):
        """
        Strategies: 
        'set'    - O(N) Time, O(N) Space
        'sort'   - O(N log N) Time, O(1) or O(N) Space
        'brute'  - O(N^2) Time, O(1) Space
        """
        target = list(x) if x is not None else self.data
        
        # --- Strategy 1: Using a Set (Fastest) ---
        if strategy == "set":
            seen = set()
            for item in target:
                if item in seen:
                    return False
                seen.add(item)
            return True

        # --- Strategy 2: Sorting (No extra data structures) ---
        elif strategy == "sort":
            target.sort()  # O(N log N)
            for i in range(len(target) - 1):
                if target[i] == target[i+1]:
                    return False
            return True

        # --- Strategy 3: Brute Force (No extra space, no sorting) ---
        elif strategy == "brute":
            n = len(target)
            for i in range(n):
                for j in range(i + 1, n):
                    if target[i] == target[j]:
                        return False
            return True
        
        else:
            raise ValueError("Unknown strategy. Use 'set', 'sort', or 'brute'.")

if __name__ == "__main__":
    # Test with a string
    obj = IsUnique("ciao")
    
    print("Original Data:")
    obj.print()

    print(f"Is Unique (Set):   {obj.IsUnique(strategy='set')}")
    print(f"Is Unique (Sort):  {obj.IsUnique(strategy='sort')}")
    print(f"Is Unique (Brute): {obj.IsUnique(strategy='brute')}")
    
    # Test with a duplicate
    obj2 = IsUnique("ciaoo")
    print(f"\nTesting 'ciaoo' (Brute): {obj2.IsUnique(strategy='brute')}")