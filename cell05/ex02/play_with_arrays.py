#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
filtered_array = [num for num in original_array if num > 5]
new_array = [num+2 for num in filtered_array]
print(",".join(str(num) for num in filtered_array))
print(new_array)