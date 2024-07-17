def trap(height):
    unit=0
    for i in range(len(height)):
        l=max(height[:i+1])
        r=max(height[i:])
        unit+=min(l,r)-height[i]
    return unit
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))