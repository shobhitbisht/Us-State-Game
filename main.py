import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("US State Game")

image = "blank_states_img.gif"

screen.addshape(image)
jim = Turtle()
jim.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()



guessed_states = []

#The game loop will run untill we guess all the 50 states
while len(guessed_states) < 50:
  
  #This will store the user input. 
  answer_state = screen.textinput(title = f"{len(guessed_states)}/50 states", prompt = "What's another state's name? ").title()

  # Check if the user input is in the states list then we will 
  # create a new turtle and send it to the x and y coordinate of that particular state
  # and ihen it will write the state name there.
  #and then will append/add the guessed state name in guessed_state list
  if answer_state in all_states:
    
    w = Turtle()
    w.hideturtle()
    w.penup()
  
    state_data = data[data.state == f"{answer_state}"]
    
    w.goto(int(state_data.x),int(state_data.y))
    
    w.write(state_data.state.item())
    
    guessed_states.append(state_data.state.item())

   
    all_states.remove(answer_state)
    
    

  elif answer_state == "Exit":
    
    #This will create a csv file of states name which we haven't guessed.
    not_guessed_state = all_states
    df = pandas.DataFrame(not_guessed_state)
    df.to_csv("states_to_learn.cs")
    break
    



  
  


