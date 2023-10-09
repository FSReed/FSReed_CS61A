# FSReed_CS61A
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
