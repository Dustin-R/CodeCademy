# CodeCademy
CodeCademy projects

This is intended to be a collection of various projects done as part of the CodeCademy course work. As such the Resporitory will be updated from time to time as I complete more courses. 

Projects included:
1. CS101: Introduction to Programming Final Project - Make a terminal game




----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. CS101: Introduction to Programming Final Project - Make a terminal game - Blog aspect

I have always been a fan of Role Playing Games ("RPG") and combat games. So I decided to create a combat based RPG. The premesis of the game is a tongue and cheeck story based on an industry I work in. 

In summary:
1. You are asked if you want to play the game 
2. If you do not accept the game ends with a specific exit message
3. If you do accept then you choose a profession/character
4. Based on your chosen professionn you are given a nemesis
5. The player and the nemesis then battle it out
6. Players manually select between a standard attack and a special
7. Nemesis selection between standard and special attacks are automated
8. Standard attacks deal damage
9. Special attacks end the fight but with some form of time line modification (delayed financial close for the player and sped up financial close for nemesis)  
10. Once the player or nemesis is defeated a message is printed declaring victory
11. Based on who one a final ending message is then given

Things I learnt:
1. Use of the delayed print function, it adds a nice old school game feel
2. Use of the input function to make use of user input
3. Became more comfortable with creating functions and when to use them. More opportunities for classes would have been good which could probably be done though expanding on the game
4. First time working with Visual Studio Code - Enjoyed using it and the way it lays and color codes everything.
5. First time working with Sypder - Used this at the end for fine tunning and testing to give it a try. I prefered the color coding of VS Code

Challenges:
1. Combat system was problematic. This was due to adding in some variability of who attacks first and alternating attacks.
2. Main challenge was to get the combat to rotate turns and stop when one of the characters ended up with zero hp
3. I had tried to make a 'while' loop work, however, this kept on causing problems where a character could get to zero hp but then the while loop would still progress to the next turn.
4. This resulted in creating a cascade of 'if' functions. This can definitely be simplified. [Note: I think using a while function here and just keeping the first and second attack may resolve the issue I was having with the while loop which was not cascaded]
5. It also took a while to make sure that the character adjusted hp was being returned properly and not just continuing - this was resolved through correct placement and indentation of the damage_calc function. 

Overall:
It was a fun exercise and something I would like to elaborate on in the future. I would probably look to do something in pygame or renpy so that some nice visuals could be added to make it a bit more interesting. 
