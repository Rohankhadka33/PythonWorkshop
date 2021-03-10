''' you live 4 miles  from university. The bus drives at 25mph but spends 2  min at each stops on the way. how long
wil the bus journey take? Alternatively,you could run to the university. you jog the first mile at 7 mph; then run
the next two at 15mph; before jogging the last at 7mph again. will this be quicker or slower than the bus?'''
#
living_miles_apart = 4
drives_velocity= 25
time_taken = ((living_miles_apart/drives_velocity)*60)
# 2 minutes in eacg stop
time_spends =20
total_time= time_taken + time_spends
print(f"total time takes by the bus is {total_time}")
jog_one=((1/7)+60)
jog_two=((2/15)+60)
jog_three=((1/7)+60)
total_walk_time =jog_three+jog_two+jog_one
print(f"Time takes by running is {total_walk_time}")

if (total_time>total_walk_time):
    print("Taking bus is slower than running")
else:
    print("taking bus is quicker than running")