from linkedlist import LinkedList

#Fill in Function
def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))
  #Write Code Here
  current = linked_list.get_head_node()
  maximum = current

  while current.get_next_node() != None:
    current = current.get_next_node()
    if current.get_value() > maximum.get_value():
      maximum = current
  return maximum.get_value()
  
  
  

#Test Cases
ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))


ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

#Runtime
runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))