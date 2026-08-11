# Review Queue

Problems to re-solve from scratch. Rule: 5 minutes, no hints, no looking at the old solution.
Solved within 5 min -> delete the line. Otherwise move the date forward a few days.

One review before the daily new problem.

## Priority 1 — got stuck on the core idea

| # | Problem | Pattern | What broke | Next |
|---|---------|---------|------------|------|
| 026 | remove_duplicates_from_sorted_array | two pointers | Tried `pop()` in a loop; index shifting | |
| 035 | search_insert_position | binary search | `mid` not excluded -> infinite loop; missed `return left` | |
| 104 | maximum_depth_of_binary_tree | recursion | Passed a counter as an argument; child values never reach the parent | |
| 110 | balanced_binary_tree | recursion | Mixed return types; needed a helper returning `(height, ok)` | |
| 112 | path_sum | recursion | Tried to subtract on the way up instead of passing down | |

## Priority 2 — logic was close, details broke

| # | Problem | Pattern | What broke | Next |
|---|---------|---------|------------|------|
| 027 | remove_element | two pointers | `slow` semantics: last kept element vs next write position | |
| 028 | find_the_index_of_the_first_occurrence | brute force | `return -1` inside the loop; sliced with the wrong length | |
| 066 | plus_one | carry | `insert` placed inside the loop instead of after it | |
| 067 | add_binary | carry | `and` vs `or` in the while condition; missing index guards | |
| 083 | remove_duplicates_from_sorted_list | linked list | Assigned `.val` instead of relinking `.next` | |
| 088 | merge_sorted_array | two pointers from end | Missing `i >= 0` guard and pointer decrements | |
| 118 | pascals_triangle | 2D build | Indexed the previous row as a whole instead of its elements | |

## Priority 3 — skeleton was given, never written from scratch

069 sqrt_x (binary search) / 094 binary_tree_inorder_traversal (recursion) /
100 same_tree (recursion) / 108 convert_sorted_array_to_bst (divide & conquer) /
121 best_time_to_buy_and_sell_stock (greedy)

## Graduated

_(move lines here, or just delete them)_