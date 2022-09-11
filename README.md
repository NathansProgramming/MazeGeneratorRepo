# MazeGeneratorRepo

IMPORTANT: It's a good idea to read this readme because it explains how the code works and how to solve the mazes yourself.

BONUS IMPORTANT: It's useful to use a type of .txt font that has "monospacing," AKA all the letters in the text are the same size. That way, mazes don't look horrifying. If you use notepad to open up these .txt files, go to "format" at the top of the screen, click on "font...", and type in "fixedsys". That should give you a font that evenly spaces everything out. If not, look up monospace fonts online. I am sure some sites will give you info about it.

DISCLAIMER: It is recommended you figure out how 3d mazes work first before trying out how 4d mazes work.

With those three out of the way, welcome to my repository of maze generation.

The simple goal of these mazes is to go from the entrance at the top left to the exit at the bottom right by traveling through the mess of directions the maze makes you go through.

There


are three files (2d, 3d, and 4d maze generator) that are designed to create mazes based on the desired dimension size. 

To use these files, download or copy the .py files in the "MazeGenerators" folder and run them on whatever app you use to run python files.

To explain how they work, it's a good idea to get a grasp of higher dimensions and what even a 3d maze is.

A 2d maze is a maze a lot of people will be used to. It's a flat maze on a piece of paper that you draw a line from the entrance to the exit. 

A 3d maze isn't a real-life corn maze or a 2d maze that is made in 3d, but rather instead a large cube that has some tunnel in it that leads from the entrance to the exit. The maze cannot only go N, S, E, and W but can also go up and down.

My code makes a 3d maze by giving you a collection of 2d slices of the 3d maze. For example, a 10x10x10 maze would give you 10 10x10 "maps" that would correspond to how far deep you are in the maze. 4d mazes are a bit more unique, however.

My code makes a 4d maze by giving you a collection of 3d mazes that have their own 2d slices. For example, a 10x10x10x10 maze would give you 10 10x10x10 mazes you could adventure in.

For a 4d maze to be possible, you need two new directions that our 3d world doesn't have, which I call "forward" and "backward".

"Forward" sends you to the next 3d maze (object), whereas "backward" sends you to the previous 3d object.

So with a 2d maze, you have to get from the top left of the maze to the bottom right.

With a 3d maze, you have to get from the top left of the highest part of the maze to the bottom right of the bottom part of the maze. This means you have to go up and down through the maze to reach the bottom level and find the exit.

A 4d maze requires you to go from the top left on the highest point of the first object to the bottom right on the lowest level of the last object. This means you have to go forwards and backward through the different 3d objects to get to the last object's bottom level and find the exit.

Did that make at least some sense? Good, because it's time we talk about some technical things with the maze generators.

2d mazes should be straightforward. cells (or 'C') mean you can walk through them. Walls (or '#') block your path, and you can't go through them. This applies to all mazes as well.

Because of how the 3d maze generator works, ups and downs don't necessarily mean they only go up or down. For example, if you find a tunnel that leads down, with the next cell below saying it's a tunnel that leads up, there could technically be a third cell below that, which also says it goes up. This means that ups and downs don't always mean you are forced to go back, so you should always check the level beneath or above in case there's another path. It's probably a good time to talk about how to use 2d slices.

In a 3d maze, when you go "down," you remember what location you were at in the last slice and go to that same coordinate in the 2d slice below. I sadly can't give you the best example of this in a readme file because of how messed up it looks, but if you look at the 3dmazes.txt file and look at "TEACUP PRISON", you should get a good idea of what going down through 2d slices means.

Also, just like how in a 2d maze if you are going forward and see a path to the right and don't have to go right, it's the same case in 3d, in which if you see an up or a down in your path, it doesn't prevent you from walking past it to go to another up or down. Remember, only walls block you.

4d mazes get a bit more hectic because of how many 2d slices are required to... 'render' them. When going forwards and backward in a 4d maze, remember what layer in the current maze you are in, where you are at in that layer, and if you have to move an object backward or forwards in the maze.

Also, be aware that just in the way that ups and downs can overwrite each other in a 3d maze, this is also the case in a 4d maze with forward and backward. Not only should you check layers of a 4d maze for overwritten ups and downs, but you should also check if an up or a down is hiding a secret forwards or backward that could help get you to the exit of a maze.

I can also prove that the 4d mazes are 4d through my idea called "The Tunnel Problem."

. Think about the idea of a 4d maze trying to be made in our world. To go "forward" and "backward" into different objects, you would have to build a tunnel that goes from one object to the next. This tunnel in a 3d world would obstruct a part of the maze, making it not a 4d maze. However, if you were to do the same forward and backward idea in a 4d world, you could effortlessly connect different objects without the tunnels obstructing any other part of the maze. Thus, this proves my 4d maze is 4d because the forward and backward tunnels do not block large parts of the maze from being used.

With the ideas of how 3d and 4d mazes work finished, Let's now talk about a bit of the code.

. I used a maze generation algorithm called "randomized Prim's algorithm," in which you start with a maze that is completely made up of walls, randomly choose one of those walls to be a cell, and then branch out the rest of the maze from that one point.

. (As explained in the py files,) You can edit the dimension's lengths in any way to customize how you want it. You can also edit how the maze looks or what colors the different tunnels represent.

. It's a good idea to read many of the comments in the py files to get a grasp on how the code works. If your computer can't use colorama, or you don't wish to install colorama, follow the commented steps at the top of each py file to remove the parts of code that use it.

Other than these points of how the generators work, have fun generating the mazes and trying to solve them yourself. I had hours of fun playing through these nightmares of tunnels and tricks, and I hope you do too. Be sure to report if you found any bugs or problems I should know about to help improve the code.

Have a great day!
