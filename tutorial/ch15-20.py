import random
import time

rows =  random.randint(1000,5000)
cols = rows


print(f"rows{'=':>8s}{rows:>3d} columns{'=':>5s}{cols:>3d}")

find_this_x= random.randint(0,cols)
find_this_y= random.randint(0,rows)

print("find_this_x={:>3d} find_this_y={:>3d}".format(find_this_x,find_this_y))

find_this = random.randint(1,100)

grid = []
for row in range(rows):
    gridRow = []
    for col in range(cols):
        if col == find_this_x and row == find_this_y:
            gridRow.append (find_this)
        else:
            gridRow.append(0)
    grid.append(gridRow)

    if row != find_this_y:
        print(f"[{'All Zeros':^16s}]")
    else:
        print("[Zeros and Plant]")

locations=[]
for location in range (rows*cols):
    locations.append(location)

locations_jumbled=locations.copy()
random.shuffle(locations_jumbled)


print("starting linear search...")
start = time.perf_counter()
for location in locations_jumbled:
    search_y = location // rows
    search_x = location % rows
    if grid[search_x][search_y] != 0:
        plant = grid[search_x][search_y]
        print(f"found {plant} planted in the grid at({search_x,search_y})")
        break
end = time.perf_counter()
print(f"Linear Search Elasped time: {end - start:.6f} seconds")

# --- Binary search
key = location
lower_bound = 0
upper_bound = len(locations)-1
found = False
 
# Loop until we find the item, or our upper/lower bounds meet
for count in range(2):
    print("starting binary search...")
    start = time.perf_counter()
    sorted_location = locations
    if(count <= 0):
        sorted_location = locations_jumbled.copy()
        sorted_location.sort();
    while lower_bound <= upper_bound and not found:
    
        # Find the middle position
        middle_pos = (lower_bound + upper_bound) // 2
    
        # Figure out if we:
        # move up the lower bound, or
        # move down the upper bound, or
        # we found what we are looking for
        if sorted_location[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif sorted_location[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True
    
    end = time.perf_counter()

    if found:
        search_y = middle_pos // rows
        search_x = middle_pos % rows
        plant=grid[search_x][search_y]
        print(f"Found (plant) planted in the grid at location (middle_pos)=() ")
    else:
        print("the plant was not in the list")
    print(f"Binary Search Elasped time: {end - start:.6f} seconds")