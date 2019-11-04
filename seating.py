import numpy as np

#class SeatAllocation:
total_seats = 24
rows = 3
cols = 8
mapping = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
seats = np.zeros((3, 8), dtype=np.int)
left_edge_index1 = 0
left_edge_index2 = 1
right_edge_index1 = 6
right_edge_index2 = 7

def allocate_seat(number_of_seats):
    #print("seats before allocation :", seats)
    result = None
    if number_of_seats == 1:
        for index in np.ndindex(3, 8):
            if seats[index] == 0:
                seats[index] = 1
                result = str(index[0]+1)+mapping.get(index[1])
                break

    elif number_of_seats == 2:
        for index in range(3):
            left_edge = seats[index][:2]
            right_edge = seats[index][-2:]
            if all(v == 0 for v in left_edge):
                result = str(index+1)+mapping.get(left_edge_index1)+","+str(index+1)+mapping.get(left_edge_index2)
                seats[index][left_edge_index1] = 1
                seats[index][left_edge_index2] = 1
                break
            elif all(v == 0 for v in right_edge):
                result = str(index+1)+mapping.get(right_edge_index1)+","+str(index+1)+mapping.get(right_edge_index1)
                seats[index][right_edge_index1] = 1
                seats[index][right_edge_index1] = 1
                break

    elif number_of_seats == 3:
        for index in range(3):
            middle = seats[index][2:5]
            if all(v == 0 for v in middle):
                result = str(index + 1) + mapping.get(2) + "," + str(index + 1) + mapping.get(3)+ "," + str(index + 1) + mapping.get(4)
                seats[index][2] = 1
                seats[index][3] = 1
                seats[index][4] = 1
                break
    elif number_of_seats == 4:
        for index in range(3):
            middle = seats[index][2:6]
            if all(v == 0 for v in middle):
                result = str(index + 1) + mapping.get(2) + "," + str(index + 1) + mapping.get(3)+ "," +str(index + 1) + mapping.get(4) + "," + str(index + 1) + mapping.get(5)
                seats[index][2] = 1
                seats[index][3] = 1
                seats[index][4] = 1
                seats[index][5] = 1
                break
            else:
                left_edge = seats[index][:2]
                right_edge = seats[index][-2:]
                if all(v == 0 for v in left_edge) and all(v == 0 for v in right_edge):
                    result = str(index + 1) + mapping.get(left_edge_index1) + "," +\
                             str(index + 1) + mapping.get(left_edge_index2) + "," +\
                             str(index + 1) + mapping.get(right_edge_index1) + "," +\
                             str(index + 1) + mapping.get(right_edge_index2)

                    seats[index][left_edge_index1] = 1
                    seats[index][left_edge_index2] = 1
                    seats[index][right_edge_index1] = 1
                    seats[index][right_edge_index2] = 1
                    break


    #print("seats after allocation :", seats)
    return result


num_of_booking = int(input("Enter number of bookings"))
for booking in range(num_of_booking):
    num_seats = int(input("Enter number of seats"))
    result = allocate_seat(num_seats)
    if result:
        print("allocated", result)
    else:
        print('Can not allocate seats')



