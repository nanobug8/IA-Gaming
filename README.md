#    Para llevar a cabo la optimizacion es necesario ejecutar el archivo optimization bajo el directorio adversarial_search-master/adversarial_search/games/                       #

Implementacion de un jugador artificial para un juego estrategia por turnos sobre un tablero.
El juego se realiza sobre un damero de 5x9 donde cada uno de los 2 jugadores tiene 3 piezas de 3 tipos distintos
cada una. Las formas de movimiento y formas de ataque viene dados por el tipo de pieza. También sobre el
tablero se encuentran obstáculos que limitan el movimiento de las piezas.

En cada turno el jugador puede realizar una de las acciones posibles con una de sus piezas. Las acciones implican
movimientos dentro del tablero y/o ataques a piezas enemigas. Los movimientos siempre se realizan antes de los
ataques, de hacerse. Los movimientos siempre se realizan de forma ortogonal, es decir horizontal o verticalmente.
Las piezas siempre deben mover a casillas que no estén bloqueadas.
Las piezas tiene una cantidad de puntos de vida (hp) asociados. Cuando una pieza ataca a otra, le hace una
cantidad de daño que es descontada de los puntos de vida de la pieza objetivo. Cuando la pieza pierde todos sus
puntos de vida, es removida del tablero. Un jugador pierde cuando queda sin piezas. 
