from typing import List

class ArraySorter:
    def __init__(self, data: List[int]) -> None:
        self.data = data

    def _swap(self, i: int, j: int) -> None:
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def display(self) -> None:
        print(self.data)

    # --- BUBBLE SORT ---
    def bubble_sort(self) -> None:
        n = len(self.data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self._swap(j, j + 1)
                    swapped = True
            if not swapped:
                break
        
    # --- SELECT SORT ---
    def select_sort(self) -> None:
        n = len(self.data)
        for x in range(n):
            min_pos = x
            for y in range(x + 1, n):
                if self.data[y] < self.data[min_pos]:
                    min_pos = y
            if min_pos != x:
                self._swap(x, min_pos)

    # --- MERGE SORT ---
    def merge_sort(self, arr: List[int] = None) -> None:
        if arr is None:
            arr = self.data
        if len(arr) > 1:
            mid = len(arr) // 2
            sinistra = arr[:mid]
            destra = arr[mid:]

            self.merge_sort(sinistra)
            self.merge_sort(destra)

            i = j = k = 0
            while i < len(sinistra) and j < len(destra):
                if sinistra[i] <= destra[j]:
                    arr[k] = sinistra[i]
                    i += 1
                else:
                    arr[k] = destra[j]
                    j += 1
                k += 1
            while i < len(sinistra):
                arr[k] = sinistra[i]
                i += 1
                k += 1
            while j < len(destra):
                arr[k] = destra[j]
                j += 1
                k += 1

    # --- QUICK SORT: EASY VERSION ---
    # This version is easy to remember but creates new lists (uses more memory)
    def quick_sort_easy(self) -> None:
        
        def _easy_recurse(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return _easy_recurse(left) + middle + _easy_recurse(right)
        
        self.data = _easy_recurse(self.data)

    # --- QUICK SORT: COMPLETE VERSION ---
    # This is the "In-Place" Hoare Partition version (memory efficient)
    def quick_sort_complete(self) -> None:
        self._quick_recursive(0, len(self.data) - 1)

    def _quick_recursive(self, low: int, high: int) -> None:
        if low < high:
            # Partition the array and get the split point
            p = self._partition(low, high)
            # Recursively sort the two halves
            self._quick_recursive(low, p)
            self._quick_recursive(p + 1, high)

    def _partition(self, low: int, high: int) -> int:
        pivot = self.data[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while self.data[i] < pivot: i += 1
            j -= 1
            while self.data[j] > pivot: j -= 1
            
            if i >= j:
                return j
            self._swap(i, j)

# --- TEST ---
if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    
    # Test Easy Version
    sorter_easy = ArraySorter(list(test_data))
    print("Original (Easy Test):")
    sorter_easy.display()
    sorter_easy.quick_sort_easy()
    print("Sorted (Easy):")
    sorter_easy.display()

    print("-" * 20)

    # Test Complete Version
    sorter_comp = ArraySorter(list(test_data))
    print("Original (Complete Test):")
    sorter_comp.display()
    sorter_comp.quick_sort_complete()
    print("Sorted (Complete):")
    sorter_comp.display()