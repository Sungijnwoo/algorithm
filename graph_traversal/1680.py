test_number = int(input())

cases = []
for i in range(test_number):
    # define trash truck maximum volume, region count
    max_volume, region_cnt = list(map(int, input().split()))
    # define distance and trash_amount from each region             
    grid = [list(map(int, input().split())) for j in range(region_cnt)]     
    cases.append([max_volume, region_cnt, grid])

result = []
for case in cases:
    max_volume, region_cnt, grid = case
    present_volume = 0
    present_distance = 0
    moving_distance = 0
    for region in grid:
        distance, trash_amount = region
        # if add trash amount over the max volume then come and back to first place (trash process region)
        if present_volume + trash_amount > max_volume:                      
            moving_distance += (distance * 3 - present_distance)
            present_distance = distance
            present_volume = trash_amount
        # if add trash amount equal the max volume then go to first place and no back
        elif present_volume + trash_amount == max_volume:
            moving_distance += (distance * 2 - present_distance)
            present_distance = 0
            present_volume = 0
        # if add trash amount not over the max voume then go next region 
        else:
            moving_distance += (distance - present_distance)
            present_distance = distance
            present_volume += trash_amount
    moving_distance += present_distance
    result.append(moving_distance)
            
for _ in result:
    print(_)