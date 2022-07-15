# MonteCarlo-Project
Monte Carlo Simulator DS 5100 Project

# Metadata
Monte Carlo Simulator by Rhea Agarwal

# Synopsis

die1=Die([4,2,5])
die2=Die([3,4,5])
die1.change_w(2,3)
print(die1.display())
die2.rolldie(5)
print(die2.display())

game1=Game([die1,die2])
game1.play(10)
print(game1.show())

analyze1=Analyzer(game1)
print(analyze1.jackpot())
print(analyze1.combo())
print(analyze1.facecount())

# API Description
