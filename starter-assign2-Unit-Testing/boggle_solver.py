class Boggle:
    def __init__(self, grid, dictionary):
        """
        Initializing the Boggle grid and dictionary.
        """
        self.grid = grid
        self.dictionary = set(dictionary)  # Store dictionary as a set for fast lookup
        self.prefixes = set()  # Set to store valid prefixes
        for word in dictionary:
            for i in range(1, len(word)):  # Add all prefixes of the word
                self.prefixes.add(word[:i])
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
        self.found_words = set()
        self.directions = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1),         (0, 1),
                           (1, -1), (1, 0), (1, 1)]  # 8 possible directions

    def getSolution(self):
        """
        Finding and returning all the valid words found in the grid.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self._search_word(i, j, "", set())  # start DFS from each cell
        return sorted(list(self.found_words))  # Sort the results for comparison in tests

    def _search_word(self, row, col, prefix, visited):
        """
        Recursive DFS for finding all valid words from a starting grid position.
        """
        # Base case: If the position is out of bounds or already visited, return
        if not (0 <= row < self.rows and 0 <= col < self.cols) or (row, col) in visited:
            return

        # Add current letter or "Qu"/"St" to prefix
        if self.grid[row][col] == "Qu" or self.grid[row][col] == "St":
            prefix += self.grid[row][col]
        else:
            prefix += self.grid[row][col]

        # If the prefix is not a valid start of any word, return early
        if prefix not in self.prefixes and prefix not in self.dictionary:
            return

        # Mark this cell as visited (create a new set to avoid affecting recursion)
        visited = visited.copy()
        visited.add((row, col))

        # If the prefix forms a valid word of at least 3 letters, add it
        if len(prefix) >= 3 and prefix in self.dictionary:
            self.found_words.add(prefix)

        # Explore all 8 adjacent cells recursively
        for direction in self.directions:
            new_row, new_col = row + direction[0], col + direction[1]
            self._search_word(new_row, new_col, prefix, visited)

def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

if __name__ == "__main__":
    main()
