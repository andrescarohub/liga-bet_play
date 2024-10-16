# main.py

from modulos.equipos import (
    registrar_equipo, equipo_mas_goles, equipo_mas_goles_contra, equipo_ultimo_puesto
)
from modulos.plantel import registrar_plantel
from modulos.estadisticas_jugadores import registrar_estadisticas_jugador, jugador_mas_faltas, jugador_mas_tarjetas_amarillas
from modulos.resultados import registrar_partido

# Función para mostrar el menú principal
def menu():
    """
    Muestra el menú principal y ejecuta las acciones seleccionadas por el usuario.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar equipo")
        print("2. Registrar plantel")
        print("3. Registrar partido")
        print("4. Registrar estadísticas de jugador")
        print("5. Ver equipo con más goles a favor")
        print("6. Ver equipo con más goles en contra")
        print("7. Ver equipo en último puesto")
        print("8. Ver jugador con más faltas")
        print("9. Ver jugador con más tarjetas amarillas")
        print("10. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            registrar_equipo()
        elif opcion == '2':
            registrar_plantel()
        elif opcion == '3':
            registrar_partido()
        elif opcion == '4':
            registrar_estadisticas_jugador()
        elif opcion == '5':
            equipo_mas_goles()
        elif opcion == '6':
            equipo_mas_goles_contra()
        elif opcion == '7':
            equipo_ultimo_puesto()
        elif opcion == '8':
            jugador_mas_faltas()
        elif opcion == '9':
            jugador_mas_tarjetas_amarillas()
        elif opcion == '10':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutamos el menú cuando se ejecuta el archivo
menu()
