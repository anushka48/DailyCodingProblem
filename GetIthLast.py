#June 15, 2022
#This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log. 
#Implement a data structure to accomplish this, with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.

#--------------------------

#Implement a list, and use subtraction to return ith last element
#Ex: [1,2,3,4,5] - get_last(2) returns 4... interpreting ith last element as ith to last

#adds to list
def record(order_id):
  order_list.extend(order_id)
  
#subtracts i from list length
def get_last(i):
  return order_list[len(order_list)-i]

#list decl
order_list = list() 
print("At any time, enter 'x' to stop menu.")

while (True):
  order_input = input("Do you want to enter an order number? y/n?")
  if (order_input == 'y'):
    order_id_in = input("Enter order id: ")
    record(order_id_in)
  elif (order_input == 'n'):
    get_last_bool = input("Do you want to retrive an entry? y/n?")
    if (get_last_bool == 'y'):
      order_idx_in = int(input("Enter order idx: "))
      print(get_last(order_idx_in))
    elif (get_last_bool == 'x'):
      break
  elif (order_input == 'x'):
    break
