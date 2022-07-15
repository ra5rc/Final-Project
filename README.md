# MonteCarlo-Project
Monte Carlo Simulator DS 5100 Project

# Metadata
Monte Carlo Simulator by Rhea Agarwal

# Synopsis
### Installing Package
git clone 
git install . 

### Importing Package

### Die Class Objects and Methods
die1=Die([4,2,5])\
die2=Die([3,4,5])\
die1.change_w(2,3)\
die1.display()\
die2.rolldie(5)\
die2.display()

### Game Class Objects and Methods
game1=Game([die1,die2])\
game1.play(10)\
game1.show()


### Analyzer Class Objects and Methods
analyze1=Analyzer(game1)\
analyze1.jackpot()\
analyze1.combo()\
analyze1.facecount()

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

##### Attributes \

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

