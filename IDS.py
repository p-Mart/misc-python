class Node:
	#Assigns arbitrary data in the node
	def assignData(self,input):
		self.data = input
		
	def __init__(self,input):
		self.node = [] #Meant to store nodes
		self.assignData(input)
	


repeated_nodes = []
depth = 0
def iterativeDeepeningSearch(root_node, current_depth):
	#Test for goal state.
	if (goalTest(root_node)):
		print "Goal Found!", root_node.data, (current_depth-1)
		return True
	
	#Add current node to the list of nodes that have been traversed.
	repeated_nodes.append(root_node)
	
	#Retrieve list of possible operators that can be applied on this node.
	operator_list = operators(root_node)
	
	#Apply all operators on this node and append them to the list of child nodes
	#if they are valid, as per missionaries and cannibals problem.
	for i in range(len(operator_list)):
		new_node_data = addTuple(root_node.data,operator_list[i])
		if(new_node_data[0] == 0 or new_node_data[0] >= new_node_data[1] and
			(3 - new_node_data[0] == 0 or 3 - new_node_data[0] >= 3 - new_node_data[1])):
			
			root_node.node.append(Node(new_node_data))
	
	#Remove any repeated nodes from the generated list of child nodes.
	if(len(root_node.node) > 0):
		removeRepeatedNodes(repeated_nodes,root_node)
	#Leave this node if no child nodes exist.
	if(len(root_node.node) == 0):
		return False
	#Traverse into the first child node recursively.
	else:
		for i in range(len(root_node.node)):
			print root_node.node[i].data, current_depth
			iterativeDeepeningSearch(root_node.node[i],current_depth+1)
	
	
	
#Removes a child node if it was already expanded in a previous node.
def removeRepeatedNodes(repeated_nodes_list,current_node):
	i = 0
	current_node_length = len(current_node.node)
	while(i < current_node_length):
		for j in range(len(repeated_nodes_list)):
			#print i, j
			if(current_node.node[i].data == repeated_nodes_list[j].data):
				del current_node.node[i]
				current_node_length -= 1
				i-=1
				if(i < 0):
					break
		i+=1
		

#Checks the goal state of the missionaries and cannibals problem
def goalTest(node):
	if (node.data == (0,0,0)):
		return True
	else:
		return False

		
def addTuple(tuple_1,tuple_2):
	result = []
	if(len(tuple_1) != len(tuple_2)):
		print "Error: Tuple length not equal"
		return 0
	else:
		for i in range(len(tuple_1)):
			result.append(tuple_1[i] + tuple_2[i])
	return tuple(result)
		
#The operators of the missionaries and cannibals problem.
def operators(node):
	operator_list = []
	if(node.data[2] == 0):
		if(node.data[0] == 2):
			operator_list.append((1,0,1))
		if(node.data[0] <= 1):
			operator_list.append((2,0,1))
			operator_list.append((1,0,1))
		if(node.data[1] == 2):
			operator_list.append((0,1,1))
		if(node.data[1] <= 1):
			operator_list.append((0,2,1))
			operator_list.append((0,1,1))
		if(node.data[0] < 3 and node.data[1] < 3):
			operator_list.append((1,1,1))
	elif(node.data[2] == 1):
		if(node.data[0] == 1):
			operator_list.append((-1,0,-1))
		if(node.data[0] >= 2):
			operator_list.append((-2,0,-1))
			operator_list.append((-1,0,-1))
		if(node.data[1] == 1):
			operator_list.append((0,-1,-1))
		if(node.data[1] >= 2):
			operator_list.append((0,-2,-1))
			operator_list.append((0,-1,-1))
		if(node.data[0] > 0 and node.data[1] > 0):
			operator_list.append((-1,-1,-1))
	
	return operator_list
	

#Missionaries and cannibals problem starting node
root_node = Node((3,3,1))
iterativeDeepeningSearch(root_node,depth) #should probs encapsulate this