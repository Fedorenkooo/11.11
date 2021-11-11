iter = 1
end_point = 1
while iter<9435:
    if iter%2==1:
        end_point*=iter
    iter+=1

print(end_point)