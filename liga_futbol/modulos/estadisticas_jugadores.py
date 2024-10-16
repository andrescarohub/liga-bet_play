# Función para obtener el jugador con más faltas cometidas
def jugador_mas_faltas():
    """
    Retorna el jugador que ha cometido más faltas en el torneo.
    """
    jugador_top = None
    max_faltas = 0
    
    for equipo, jugadores in estadisticas_jugadores.items():
        for jugador, stats in jugadores.items():
            if stats['faltas_cometidas'] > max_faltas:
                jugador_top = (equipo, jugador)
                max_faltas = stats['faltas_cometidas']
    
    if jugador_top:
        print(f"El jugador con más faltas es {jugador_top[1]} del equipo {jugador_top[0]} con {max_faltas} faltas.")
    else:
        print("No hay estadísticas de faltas disponibles.")

# Función para obtener el jugador con más tarjetas amarillas
def jugador_mas_tarjetas_amarillas():
    """
    Retorna el jugador que ha recibido más tarjetas amarillas.
    """
    jugador_top = None
    max_tarjetas_amarillas = 0
    
    for equipo, jugadores in estadisticas_jugadores.items():
        for jugador, stats in jugadores.items():
            if stats['tarjetas_amarillas'] > max_tarjetas_amarillas:
                jugador_top = (equipo, jugador)
                max_tarjetas_amarillas = stats['tarjetas_amarillas']
    
    if jugador_top:
        print(f"El jugador con más tarjetas amarillas es {jugador_top[1]} del equipo {jugador_top[0]} con {max_tarjetas_amarillas} tarjetas.")
    else:
        print("No hay estadísticas de tarjetas amarillas disponibles.")
