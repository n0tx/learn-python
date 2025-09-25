"""
Tulis fungsi kuadrat_list(nums) 
yang menerima daftar angka nums
dan mengembalikan daftar baru
yang berisi kuadrat tiap angka
kuadrat_list([2, 3, 5]) -> [4, 9, 25]
"""

def kuadrat_list(nums: list[int]) -> list[int]:
    return [ i * i for i in nums]

print(kuadrat_list([2, 3, 5]))