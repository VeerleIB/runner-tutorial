# Runner Tutorial
### Welcome to my journey of discovering Pygame for the first time!
This is a small endless runner game I created while learning the Pygame libary with the Ultimate Pygame Tutorial.


![Screenshot_Gameplay](graphics/screenshot_gameplay.png)

_By [Veerle B](https://github.com/VeerleIB)_

## Table Of Content

- [Installation](#installation)
    - [How to play]
- [Process](#process)
  - [Sources](#sources)
  - [Learned](#learned)
  - [Future improvements](#future-improvements)
  - [Final thoughts](#final-thoughts)

# Installation
### How to play
You can start the game by either copying the repository and running it in the terminal with the command:
`$ python game.py`

Or directly by running the `EndlessRunner.exe`.

Press the **space** key to start playing and jump.

# Process
A quick reflection of the process.
### Sources
Thru this learning process, I've relied on tutorials, documentation and community forums to keep myself sane. 

List of resources:
- [The ultimate introduction to Pygame](https://www.youtube.com/watch?v=AY9MnQ4x3zk_)
- [Pygame documentation](https://www.pygame.org/docs/)

### Learned
I've learned a ton! Among the 2 Python project i've tackled so far, this one stands out as the most exciting and challenging to date. Learning a new libary like Pygame added an extra layer of challenge, pushing me to learn and tackle the fundamentals even more.

##### Here's a quick list of what i've learned: 
- The basics of Pygame libary
  * Rendering the screen, working with surfaces, utilizing rects for positioning and collision detection, managing timers, implementing simple animations, and much more.
- Enhancing core concepts
  * Usage of variables, understanding of new methods, such as: len, randint and choice, introduction and exploration of classes

While some of these concepts may still feel a bit shaky, the exposure to new techniques has improved my understanding immensily. And like everyone when learning something new, I realise: _“The more I know, the more I realize I know nothing.”_

### Future improvements
In the future, I hope to look back on this an either laugh or cringe. And that's perfectly okay—it's all part of the learning process! Looking ahead, there are several areas I'd like to refine:
##### Improved enemy spawning mechanism
Currently, I'm using the choice function from the random module to determine the type of obstacle/enemy to spawn. However, this feels restrictive in what it's supposed to achieve. Allocating a 1/4 chance to spawn a fly could be done in a more efficient way instead of writing choice(['fly','snail','snail','snail']).
##### Enhancing player input handling
The player jumping is controlled directly via pygame.key.get_pressed(). While functional, in the future, I would like to utilize the event loop. Not only is it more efficient, but it's also applicable to the goal I want to work toward: coding in a game engine, which usually uses event loops to handle player inputs.
#### Adding 'settings'
I would like to incorporate settings the player could adjust, like volume control and diffuctly, to add an extra layer of polish.
