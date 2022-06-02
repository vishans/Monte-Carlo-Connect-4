# Monte-Carlo-Connect-4

<img src="first.png">

An old project of mine, back when I was learning game theory. A Monte Carlo simulation is used by the computer to play against a human.

<img src="animation.gif">

## Conclusion
The simulation is not really effective in this situation. <br>
*N*, the number of simulations run on each turn, is small. <br>
A higher *N* requires **too much computation** and is **slow**.<br>
I, therefore, implemented a **minimax alogorithm** as well. The minimax algorithm is used by <br>default, since it is the most performant. To switch the algorithm used by the AI, use the <br><code>play</code>
method of the AI class.



