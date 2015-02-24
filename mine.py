print "Hello, world - time for minesweeper fun!"

class Grid:

	#def __init__(self):
		#add initial values

	def compute_reference_grid(master_grid):
		for cell in master_grid:
			#calculate number of adjacent m squares and store the value
		   	reference_grid = [['0','2','m'], ['1','m','2'], ['0','1','0']]
		
	def compute_success_grid(reference_grid):
		#detemine how grid looks on successful completion of game
		success_grid = reference_grid
		for row_in_success_grid, row_in_reference_grid in success_grid, reference_grid:
			for cell_success, cell_reference in row_in_success_grid, row_in_reference_grid:  
				if cell_reference == 'm':
					cell_success = 'f'

		success_grid = [['0','2','f'], ['1','f','2'], ['0','1','0']]

	def check_location(user_option1, user_option2, user_option3, user_grid, reference_grid):
		if user_option1 == 'f':
		 	flag_location(user_grid)
		else:
			#find the location on reference_grid
			if reference_grid[user_option2][user_option3] == 'm':
				#user has stepped on a minefield
				print "minefield alert"
				return -1
	        user_grid[user_option2][user_option3] = reference_grid[user_option2][user_option3] 
			#compare user_option location on user_grid and reference_grid
			#add the value in user_grid
			
		player_state = check_if_winner(user_grid)
		return player_state

	def flag_location(user_option2, user_option3, user_grid):
		#flag location as f
		user_grid[user_option2][user_option3] = 'f'

	def check_if_winner(user_grid, success_grid):
		if cmp(user_grid, success_grid):
			#player has won the game
			return 1
		else:
			#player can continue game
			return 0



class Player:

	#def __init__(self):
		#add initial values

	def display_grid(given_grid):
		#display the 2D list
		for each_row in given_grid:
			for cell in every_row:
				print str(cell),  #trailing comma to ensure white space
			print 


	def play(winner):
		while(winner == 0):
			print "Enter your option"
			print "For example: open = o(x axis, y axis) or flag = f(x axis, y axis)"
			#0 for open and 1 for flag
			user_option1 = 1
			user_option2 = 0 
			user_option3 = 1

			winner = g.check_location(user_option1, user_option2, user_option3, user_grid, master_grid)
			display_grid(user_grid)
			if winner == -1:
				print NO_SUCCESS_MSG
			elif winner == 1:
				print SUCCESS_MSG



class Game:

	SUCCESS_MSG = "Wow, you cleared the minefield! Game over!"
	NO_SUCCESS_MSG = "Oops, you stepped on a mine! Game over!"

	#def __init__(self):
		#add initial values

	print "Enter the minefield layout"
	#accept it in a 2D list - master_grid
	master_grid = [['x','x','m'], ['x','m','x'], ['x','x','x']];
	
	#compute reference grid
	compute_reference_grid(master_grid)
	compute_success_grid(master_grid)

	#initialize user grid 
	user_grid = [['x','x','x'], ['x','x','x'], ['x','x','x']]
	#show user grid
	display_grid(user_grid)

	#initial state of user
	winner = 0 

	play(winner)
    
	print "Hope you enjoyed the game =)"








