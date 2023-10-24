# Course website  
https://inst.eecs.berkeley.edu/~cs61a/fa20/  
  
# General Introduction  
Actually this is my first time to create a repo and take care of it like it's my baby lol.  
Big thanks to UCB CS 61A, which gives me the opportunity to dive into the world of CS.  
This is much more like a repo to record my progress, so all these texts seem to be written just for me myself lol.  
If someday later I can see these words again, hope I have been doing what I want to do at that time.  
That's all! At least for now!  
Typed at 2023-09-13  
  
# Here are some problems that I failed to solve on my own:  
1. The pawssible_patches() function in Project 02.  
2. The riffle() function in lab05.  
3. The merge() function in disc06.  
(Failed to finish merge function in disc06, but the reason is that I wrote the word "value" as word "vaule". That's ridiculous.)  
4. The permutations() function in hw04.
(Forget that assigning a new name to an existing list doesn't make a new list. Thus any operation of the new name causes the change to the previous list.)  
5. The scale() function in lab07.  
(The use of map! Using next(iterator) will cause the StopIteration error.)  

# Notes during the project:
1. In Ants Project, when implementing the FireAnt class inherited from Ant, the reduce_armor method is asked to inherite from Ant class but not Insect class. And when calling reduce_armor method on every bee in current_place.bees, we should use a copy of current_place.bees, or we may skip some bees in the current_place!  
2. In Ants Project, when initializing the HungryAnt class, I assign self.armor = armor, and self.digesting = 0, but this breaks the abstraction barrier! Digesting is an instance attribute added to HungryAnt class, but armor should be initialized in Ant class!  
3. In Ants Project, in optional question 4, you can see a lot of debug prints! Check the annotation line in make_scary function. If you uncomment that line, and run python ok on optional4, you can see when the bee is no longer afraid, this line will assign the wrong method to the bee.action. 

# For Scheme Project:  
1. Problem 01 almost stopped me at the very beginning of this project! The mutual recursive call between scheme_read and read_tail is sort of confusing. Need to see the given doctest to gain a better understanding of what this part is doing, and especially, what would be printed when calling these two functions.  
Think about this:    
>>> read_tail(Buffer(tokenize_lines(['(1 2 3)']))) # Type SyntaxError if you think this errors  
What would python print?  
  
2. Problem 04: I don't know how to use the map method provided in Pair class, all these lines you can see in main branch do work, but in Smart_Solutions branch(Yes it's so tricky for me and I think I need a new branch to save it), you can see all these lines can be simplified into just one line with map method of Pair class.  
  
3. Problem 06: quote is like a notation, telling the interpreter to pack up the entire expression behind it. How to implement it? We can make a new pair, whose first is the original expression, and rest is nil. This pair is called QUOTE_ME, then read the quote expression will create a pair like: Pair('quote', QUOTE_ME). If we don't use this, the interpreter won't know where this quoted expression ends.  
