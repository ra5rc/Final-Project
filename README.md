# MonteCarlo-Project
Monte Carlo Simulator DS 5100 Project

# Metadata
Monte Carlo Simulator by Rhea Agarwal

# Synopsis
### Die Class Objects and Methods
die1=Die([4,2,5])\
die2=Die([3,4,5])\
die1.change_w(2,3)\
die1.display()\
die2.rolldie(5)\
die2.display()\

### Game Class Objects and Methods
game1=Game([die1,die2])\
game1.play(10)\
game1.show()\


### Analyzer Class Objects and Methods
analyze1=Analyzer(game1)\
analyze1.jackpot()\
analyze1.combo()\
analyze1.facecount()\

# API Description

### Die Class \
 """\
    A die has N sides, or “faces”, and W "weights",\
    stored in a dataframe that can be rolled to select\ 
    a face.\ 
  
    Attributes:\
    A die object with assigned faces and weights.\
    
    Methods:\
    __init__\
    change_w\
    rolldie\
    display\
   
    """\
##### Methods \
__init__\
 """\
   Initialize the Die from faces and weights.\ 
       
   Input Arguments:
   n must be an array of floats, integers or strings.
   w can be an array or value of floats or integers. 
   If no weight is specified, w will default to 1.0.
 """
change_w\
rolldie\
display\

##### Attributes \

### Game Class \
##### Methods \
__init__\
play\
show\

##### Attributes \


### Analyzer Class \
##### Methods \
__init__\
jackpot\
combo\
facecount\

##### Attributes \


# Manifest
