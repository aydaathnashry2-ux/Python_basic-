A = [10, -20, -5, 30, 0, 40, 0]
pos_counter = 0
neg_counter = 0
zero_counter = 0
for num in A :
    if num > 0:
      pos_counter += 1
    elif num < 0:
       neg_counter += 1
    else : 
       zero_counter += 1
print(pos_counter)
print(neg_counter)
print(zero_counter)
