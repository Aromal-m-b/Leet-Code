class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        # Get dimensions of the grid
        num_rows, num_cols = len(grid), len(grid[0])
      
        # Initialize result grid with zeros
        result = [[0] * num_cols for _ in range(num_rows)]
      
        # Iterate through each element in the original grid
        for row_idx, row in enumerate(grid):
            for col_idx, value in enumerate(row):
                # Convert 2D position to 1D position
                flat_position = row_idx * num_cols + col_idx
              
                # Calculate new position after k shifts
                new_flat_position = (flat_position + k) % (num_rows * num_cols)
              
                # Convert 1D position back to 2D coordinates
                new_row, new_col = divmod(new_flat_position, num_cols)
              
                # Place the value at the new position
                result[new_row][new_col] = value
      
        return result