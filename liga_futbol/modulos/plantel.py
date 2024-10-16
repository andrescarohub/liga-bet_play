# equipo.py
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_favor = 0
        self.goles_contra = 0
        self.partidos_jugados = 0

    def actualizar_resultado(self, goles_favor, goles_contra):
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
        self.partidos_jugados += 1

        if goles_favor > goles_contra:
            self.puntos += 3  # Victoria
        elif goles_favor == goles_contra:
            self.puntos += 1  # Empate
        # Si pierde, no se suman puntos