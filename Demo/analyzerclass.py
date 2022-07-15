#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import random

class Die():
    """
    A die has N sides, or “faces”, and W "weights",
    stored in a dataframe that can be rolled to select 
    a face. 
  
    Attributes:
    A die object with assigned faces and weights.
    
    Methods:
    __init__
    change_w
    rolldie
    display
   
    """
    _diedf=pd.DataFrame({'faces':[],'weights':[]})
    
    def __init__(self, n, w = 1.0):
        
        """
        Initialize the Die from faces and weights. 
       
        Input Arguments:
        n must be an array of floats, integers or strings.
        w can be an array or value of floats or integers. 
        If no weight is specified, w will default to 1.0.
        """
        self.n=n
        self.w=w
        _newdie = pd.DataFrame({'faces': n, 'weights': w})
        self._diedf = pd.concat([self._diedf, _newdie], ignore_index=True)

    def change_w(self, faces, weights):
        """
        The function to change the weight of a specified face.
  
        Parameters:
           faces, int, float, or string.
           weights, int or float.
           
        Returns:
            Specifies whether face is in array of values already.
            Changes type of weight to floaat if not already.
            Changes weight at specified face value.
            
        """
        if (not (faces in list(self._diedf['faces']))):
            raise ValueError('Face not in die.')
        else:
            self._diedf.at[self._diedf.index[self._diedf.faces == faces],'weights']=float(weights)

    def rolldie(self, number=1):
        """
        The function to roll a die object a number of times according to weight.
        
        Parameters:
        number, int or float
        
        Returns:
        An array of face values chosen randomly a specified number of times.
        """
        roll= random.choices(self._diedf['faces'].values, self._diedf['weights'].values, k=number)
        return(roll)
          
    def display(self):
        """
        The function to display a dataframe of the faces and weights of a die.         
        
        Returns:
        A dataframe with the faces and weights of a die.               
        
        """
        
        return(self._diedf)
class Game():  
    """
    A game object consists of one or more die objects that 
    can be rolled to output a number of faces. 
  
    Attributes:
    A game object with at least one die.
    
    Methods:
    __init__
    play
    show  
  
    """  
    
    def __init__(self, games):
        """
        Initialize a game from die objects. 
       
        Input Arguments:
        Games must be a list of at least one die objects.
        """
        self.games=games
       
    def play(self, ntimes):
        """
        The function to play one or more die a specified amount of times
        
        Parameters:
        ntimes, int or float
        
        Returns:
        Rolls one or more die a specified number of times and stores results into a dataframe. 
        """
           
        rolllist=[]
        for x in range(0, len(self.games)):
            rolllist.append(self.games[x].rolldie(ntimes))
        dienames=[]
        [dienames.append("Die"+str(x) )  for x in range(0, len(self.games))] 
        self._rolldf= pd.DataFrame(rolllist, index = dienames).T
        self._rolldf.index.name ='Roll Number'

   
    def show(self, form='wide'):
        """
        The function to display the outcomes of a game in wide or narrow dataframe. 
        
        Parameters:
        form, as 'wide'(default) or 'narrow', else raises exception. 
        
        Returns:
        A dataframe of game results as wide or narrow otherwise raises exception. 
        """
        if form == 'narrow':
            return(self._rolldf.unstack().to_frame().rename_axis(index=["Die Number", "Roll Number"]))
                           
        elif form =='wide':
            return(self._rolldf)
        
        elif (form != 'wide') or (form != 'narrow'):
            raise Exception('Form not accepted. Continue with wide or narrow.')
            

class Analyzer():
    """
    An Analyzer object consists of one or more game 
    objects with a results dataframe and can compute statistical 
    properties. 
  
    Attributes:
    A analyze object with a specified game. 
    
    Methods:
    __init__
    jackpot
    combo
    facecount
  
    """ 
    def __init__(self, gameobj):
        """
        Initialize the Analyzer object from a game. 
       
        Input Arguments:
        gameobj must be a game with at least one die 
        that has been played.
    
        """
        self.gameobj=gameobj
        self.gameobjdf = self.gameobj.show()

    def jackpot(self):
        """
        The function checks each roll for the same face 
        outputted and counts the number of rolls where the 
        face values are all equal.
        
        Returns:
        The length of a dataframe of jackpot rows as an integer.
        """
        
        self.jackresultdf=self.gameobjdf[self.gameobjdf.nunique(axis=1).eq(1)]
        return(len(self.jackresultdf))
    
    def combo(self):
        """
        The function computes the number of times each unique combination of faces rolled occurs.
        
        Returns:
        A dataframe of each unique combination of faces rolled totaled.
        """
        self.uni= (self.gameobjdf.value_counts()).to_frame().rename(columns={0: "Counts"}, level = 0)        #.rename_axis(index=["Die Number", "Count"])
        return(self.uni)
    
    def facecount(self):
        """
        The function counts the number of times every face appears in each roll.
        
        Returns:
        A dataframe of each face totaled for every roll. 
        
        """
        return(self.gameobjdf.apply(pd.Series.value_counts, axis=1).fillna(0))
            



