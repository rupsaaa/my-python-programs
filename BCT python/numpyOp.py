import numpy as np
arr = np.arange(1, 11)                        
matrix = arr.reshape(2, 5)                    
print(f"Mean: {np.mean(arr)}, Median: {np.median(arr)}, STD: {np.std(arr)}")
print(arr[arr > 5])