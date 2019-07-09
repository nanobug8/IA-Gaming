#    Para llevar a cabo la optimizacion es necesario ejecutar el arvhico optimization bajo   #
#    el directorio adversarial_search-master/adversarial_search/games/                       #

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
puntos de vida, es removida del tablero. Un jugador pierde cuando queda sin piezas. Cuando un jugador pierde,
el otro jugador gana.

Los tipos de piezas y sus reglas son los siguientes. Muchas propiedades de las piezas y sus acciones se dan definen
como parámetros (e.g. k_hp), cuyos valores deberán ser asignados por la implementación del juego.
• Knight: El caballero tiene k_hp puntos de vida inicialmente. Puede mover hasta 2 casillas por turno.
– Si se mueve 2 casillas en línea, puede atacarse a un enemigo en la tercera casilla alineada, con un
daño de k_dmg_1.
– Con cualquier otro movimiento, puede atacar a una de las piezas enemigas adyacentes ortogonalmente
con daño k_dmg_2.
– Si no mueve, puede atacar a todas las piezas enemigas adyacentes ortogonalmente con daño k_dmg_3.
• Mage: El mago tiene m_hp puntos de vida inicialmente. Puede mover hasta 3 casillas por turno.
– Si mueve, cura a todas las piezas aliadas adyacentes ortogonalmente por m_dmg_1 puntos de vida. La
cantidad de puntos de vida nunca debe superar la cantidad de puntos de vida inicial de cada pieza.
El mago no se cura a sí mismo.
Agustín Castillo & Leonardo Val Pág. 1
Proyecto de Inteligencia Artificial 1 2019 Primer semestre 2019
– Si no mueve, puede atacar a una pieza oponente que esté a una distancia de Manhattan mayor de
m_dist_1 con un daño m_dmg_2.
• Archer: El arquero tiene a_hp puntos de vida inicialmente. Puede mover hasta 3 casillas por turno.
– Siempre puede atacar a todas las piezas oponentes visibles que estén en la misma diagonal u ortogonal,
a una distancia mayor que a_dist_2.
– Si no mueve, el daño de su ataque es de a_dmg_1.
– Si mueve, el daño de su ataque es de a_dmg_2.
Ademas de implementar la lógica del juego y los jugadores artificiales, también deben encontrarse los valores
apropiados para los 12 parámetros del juego (puntos de vida, puntos de daño, y distancias). Los parámetros y
sus dominios son:
• Knight: k_hp ∈ [1-30], k_dmg_1 ∈ [1-30], k_dmg_2 ∈ [1-30], k_dmg_3 ∈ [1-30].
• Mage: m_hp ∈ [1-30], m_dmg_1 ∈ [1-30], m_dmg_2 ∈ [1-30], m_dist_1 ∈ [1-9].
• Archer: a_hp ∈ [1-30], a_dmg_1 ∈ [1-30], a_dmg_2 ∈ [1-30], a_dist_2 ∈ [1-9].
Los valores para dichos parámetros se deben optimizar de forma tal de lograr los siguientes objetivos:
1. La duración promedio de las partidas sea de 18 turnos.
2. El juego este nivelado, osea que ambos jugadores tengan una probabilidad similar de ganar.
