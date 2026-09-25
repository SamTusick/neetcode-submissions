class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, col, 3x3 grid hashmaps
        row_val, col_val, box_val = {}, {}, {}
        ans = True

        # check each row and col for dups
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                # skip if empty
                if col == '.':
                    continue
                # checking row
                if col not in row_val:
                    row_val[col] = 1
                else:
                    return False

                # checking column 
                # storing val+j as dict key
                if (col, j) not in col_val: 
                    col_val[(col, j)] = 1
                else:
                    return False

                # calculate which box
                box = (i // 3) * 3 + (j // 3)

                # checking box
                if (col,box) not in box_val:
                    box_val[(col, box)] = 1
                else:
                    return False

            # clear after each row
            row_val.clear()
            ans = True
        return ans
        


        