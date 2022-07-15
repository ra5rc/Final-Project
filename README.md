# Final-Project
Monte Carlo Simulator DS 5100 Project

# Metadata
Monte Carlo Simulator by Rhea Agarwal

# Synopsis
### Installing Package
git clone https://github.com/ra5rc/Final-Project \
git install . 

### Importing Package
from Demo.dieclass import Die  
from Demo.gameclass import Game \
from Demo.analyzerclass import Analyzer 

### Die Class Objects and Methods

``` python
die1=Die([4,2,5]) # Initializing the die
die2=Die([3,4,5])
die1.change_w(2,3) # Changing the weight of face 2 to 3 from default 1
die1.display() # Displaying die contents
die2.rolldie(5) # Random sample of 5 numbers from faces
die2.display() # Outputting results
```
### Game Class Objects and Methods
```python
game1=Game([die1,die2]) # Initializing the game
game1.play(10) # Rolling each die in the game 10 times
game1.show() # Displaying the results
```

### Analyzer Class Objects and Methods
```python
analyze1=Analyzer(game1) # Initializing the analyzer object
analyze1.jackpot() # Computing number of rolls where all faces are equal
analyze1.combo() # Computing number of each unique combination
analyze1.facecount() #Computing the number of each face occurrence for every roll
```
# API Description

### Die Class 
 ```
    Description:
    A die has N sides, or “faces”, and W "weights",
    stored in a dataframe that can be rolled to select 
    a face.
  
    Attributes:
    A die object with assigned faces and weights.
    
    Methods:
    __init__()
    change_w()
    rolldie()
    display()
   
  ```
##### Methods 
\_\_init\_\_()

 ```
   Description:
   Initialize the Die from faces and weights. 
       
   Input Arguments:
   n must be an array of floats, integers or strings.
   w can be an array or value of floats or integers. 
   If no weight is specified, w will default to 1.0.
 ```
 
change_w()
```
    Description:
    The function to change the weight of a specified face.
  
    Parameters:
    faces, int, float, or string.
    weights, int or float.
           
    Returns:
    Specifies whether face is in array of values already.
    Changes type of weight to floaat if not already.
    Changes weight at specified face value.
            
```
rolldie()
```
    Description:
    The function to roll a die object a number of times according to weight.
        
    Parameters:
    number, int or float
        
    Returns:
    An array of face values chosen randomly a specified number of times.
```
display()
```
     Description:
     The function to display a dataframe of the faces and weights of a die.         
        
     Returns:
     A dataframe with the faces and weights of a die.               
        
```
##### Attributes 
```
n: array of floats, integers, or strings 
w: array of floats or integers 
```
### Game Class 
```
    Description:
    A game object consists of one or more die objects that 
    can be rolled to output a number of faces. 
  
    Attributes:
    A game object with at least one die.
    
    Methods:
    __init__()
    play()
    show()
  
```
##### Methods 
\_\_init\_\_()
```
    Description:
    Initialize a game from die objects. 
       
    Input Arguments:
    Games must be a list of at least one die objects.
```
play()
```
    Description:
    The function to play one or more die a specified amount of times
        
    Parameters:
    ntimes, int or float
        
    Returns:
    Rolls one or more die a specified number of times and stores results into a dataframe. 
     
```
show()
```
    Description:
    The function to display the outcomes of a game in wide or narrow dataframe. 
        
    Parameters:
    form, as 'wide'(default) or 'narrow', else raises exception. 
        
    Returns:
    A dataframe of game results as wide or narrow otherwise raises exception. 
     
```
##### Attributes 
```
games: a list of die objects
```
### Analyzer Class 
```
    Description:
    An Analyzer object consists of one or more game 
    objects with a results dataframe and can compute statistical 
    properties. 
    
    Attributes:
    A analyze object with a specified game. 
    
    Methods:
    __init__()
    jackpot()
    combo()
    facecount()
```
##### Methods 
\_\_init\_\_()
```
    Description:
    Initialize the Analyzer object from a game. 
       
    Input Arguments:
    Gameobj must be a game with at least one die 
    that has been played.
    
```
jackpot()
```
    Description:
    The function checks each roll for the same face 
    outputted and counts the number of rolls where the 
    face values are all equal.
         
    Returns:
    The length of a dataframe of jackpot rows as an integer.
     
```
combo()

```
    Description:
    The function computes the number of times each unique combination of faces rolled occurs.
        
    Returns:
    A dataframe of each unique combination of faces rolled totaled.
     
```
facecount()
```
    Description:
    The function counts the number of times every face appears in each roll.
        
    Returns:
    A dataframe of each face totaled for every roll. 
     
```

##### Attributes 
```
gameobj: game object
gameobjdf: dataframe of game object roll results
jackresultdf: dataframe of jackpot results
uni: dataframe of combination counts

```

# Manifest
Demo Package:
\_\_init\_\_\
dieclass.py\
gameclass.py\
analyzerclass.py\
ProjectTest.py\

carlo_output.txt\
FinalProjectSubmission.ipynb\
setup.py\

