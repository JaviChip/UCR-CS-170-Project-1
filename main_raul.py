#UI

from problem_raul import Problem

def main ():

    print("\nHello there, this is eight-puzzle solver for CS-170 , Intro to AI \n")

    print ("Select whether you would like to run the default puzzle or a custom puzzle \n \nEnter 0 for Default or 1 for Custom \n")

    val = input("Enter Here: ")

    val = int(val)

    if val == 0:

        print ("\n  You have selected the Default puzzle:\n \n  The following is the initial state \n ")

        initialState = [[1,2,3], [4, 5, 6], [7,0,8]]

        for row in initialState:

            print("  " +"  " +"  " + "  " + " ".join(str(num) for num in row))

        print("\n  Here is the goal state we are trying to find: \n")

        goalState = [[1,2,3], [4,5,6], [7,8,0]]

        for row in goalState:

            print("  " +"  " +"  " + "  " + " ".join(str(num) for num in row))


        print("\n  Choose an algorithm to solve the puzzle \n \n")

        print ("  Option 1: Uniform Cost Search \n \n  Option 2: A* with the Misplaced Tile heuristic \n \n  Option 3: A* with the Euclidean Distance heuristic \n \n ")

        selected_algorithm = input("  Enter 1 , 2 , or 3 for corresponding algorithm: ")

        selected_algorithm =int(selected_algorithm)

        if selected_algorithm == 1:

            # TO DO :
            # Call Problem Function Here

            print("\n  You Selected: " + str(selected_algorithm) + "\n")

        elif selected_algorithm == 2:

            # TO DO :
            # Call Problem Function Here

            print("\n  You Selected: " + str(selected_algorithm) + "\n")

        elif selected_algorithm == 3:

            # TO DO :    
            # Call Problem Function Here
            problem = Problem(initialState, goalState, selected_algorithm);
            problem.solve()

            print("\n  You Selected: " + str(selected_algorithm) + "\n")

        else:
            print("\n  Invalid Choice Entry -> END OF PROGRAM\n")



    elif val == 1:

        print("\n  You have selected custom puzzle:")

        print("\n  Important Note: 0 is represented as an empty space in the eight-puzzle. Only valid input numbers are 1-8 used once each\n")

        #  User inputs their own initial state row by row

        initialState = []

        print("\n  Enter the initial state of the puzzle row by row (3 rows, each containing 3 numbers separated by spaces): \n")

        for i in range(3):

            while True:

                row_input = input(f"\n  Enter the numbers for row {i+1} separated by spaces: ")

                row = row_input.split()

                if len(row) != 3:

                    print("\n  Invalid input. Please enter exactly 3 numbers separated by spaces.")

                elif all(num.isdigit() for num in row) and all(0 <= int(num) <= 8 for num in row):

                    row = [int(num) for num in row]

                    initialState.append(row)

                    break

                else:

                    print("\n  Invalid input. Please enter numbers between 0 and 8.\n \n")


        # Print the user-defined initial state

        print("\n  Here is the custom initial state you provided:\n")

        for row in initialState:

            print("  " + "  ".join(str(num) for num in row))

        print("\n  Here is the goal state we are trying to find:\n")

        goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


        for row in goalState:

            print("  " + "  ".join(str(num) for num in row))

        print("\n  Choose an algorithm to solve the puzzle\n")

        print("\n  Option 1: Uniform Cost Search\n")

        print("\n  Option 2: A* with the Misplaced Tile heuristic\n")

        print("\n  Option 3: A* with the Euclidean Distance heuristic\n")

        selected_algorithm = input("\n  Enter 1, 2, or 3 for the corresponding algorithm: ")

        selected_algorithm = int(selected_algorithm)

        if selected_algorithm == 1:

            # TO DO: Call Problem Function Here

            print("\n  You Selected: " + str(selected_algorithm) + "\n")

        elif selected_algorithm == 2:

            # TO DO: Call Problem Function Here

            print("\n  You Selected: " + str(selected_algorithm) + "\n")

        elif selected_algorithm == 3:

            # TO DO: Call Problem Function Here
            problem = Problem(initialState, goalState, selected_algorithm);

            print("\n  You Selected: " + str(selected_algorithm) + "\n")

        else:
            
            print("\n  Invalid Choice Entry -> END OF PROGRAM\n")

    
    else :

        print ("\nInavlid Choice Entry -> END OF PROGRAM\n")


if __name__ == "__main__":

    main()