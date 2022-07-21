## A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. Social distancing guidelines require that every diner be seated such that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty. There are currently M diners seated at the table, the ith of whom is in seat S(i). No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

## Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.


# Checking if all values are equal to user input
def check(list_in, list_pat):
    unique_list = []     
    for x in list_in:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    list_pat.sort()
    #Loop through list
    for x in unique_list:  
        # Compare with all the values with user input
        if(set(unique_list).issubset(set(list_pat))):
            return True 
        elif unique_list == list_pat:
            return True 
        else:
            return False

# Calculating possible diners
seats = list(range(1,N+1))   
seating_list = dict.fromkeys(seats, "Empty")
restricted_seats = []
for i in S:
    seating_list[i] = "Filled"
    restricted_seats.extend((range((max(1,i-K)),(min(i+K+1,N)))))
    restricted_seats.remove(i)
for j in restricted_seats:
    seating_list[j] = "Restricted"
empty_seats = [k for k, v in seating_list.items() if v == 'Empty']
for k in empty_seats:
    empty_seats_check = list(range((max(1,k-K)),(min(k+K+1,N))))
    if k in empty_seats_check:
        empty_seats_check.remove(k)
    seating_list_check = [seating_list[i] for i in empty_seats_check]
    list_pat = ['Empty','Restricted']
    if check(seating_list_check,list_pat):
        seating_list[k] = "Diner"
seats_available = [k for k, v in seating_list.items() if v == 'Diner']
print(len(seats_available))