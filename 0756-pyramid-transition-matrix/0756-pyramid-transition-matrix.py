from functools import cache
from collections import defaultdict
from itertools import pairwise, product
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Build a mapping from (left_block, right_block) -> list of possible top blocks
        transitions_map = defaultdict(list)
        for transition in allowed:
            left_block, right_block, top_block = transition[0], transition[1], transition[2]
            transitions_map[left_block, right_block].append(top_block)
      
        @cache
        def can_build_pyramid(current_level: str) -> bool:
            # Base case: if we reach the top (single block), pyramid is complete
            if len(current_level) == 1:
                return True
          
            # Build all possible options for the next level
            next_level_options = []
          
            # For each adjacent pair in current level, find possible blocks above them
            for left_block, right_block in pairwise(current_level):
                possible_blocks = transitions_map[left_block, right_block]
              
                # If no valid block can be placed above this pair, pyramid cannot be built
                if not possible_blocks:
                    return False
              
                next_level_options.append(possible_blocks)
          
            # Try all combinations of blocks for the next level
            # product(*next_level_options) generates all possible combinations
            for next_level_combination in product(*next_level_options):
                next_level_string = ''.join(next_level_combination)
                if can_build_pyramid(next_level_string):
                    return True
          
            return False
      
        # Start building from the bottom
        return can_build_pyramid(bottom)