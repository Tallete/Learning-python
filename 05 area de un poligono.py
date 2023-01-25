"""
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
"""

class triangulo:
    def __init__(self, base,altura):
        self.base = base
        self.altura = altura
    def area (self):
        return self.base*self.altura/2

class rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area (self):
        return self.base*self.altura

class cuadrado:
    def __init__(self,lado,):
        self.lado = lado
    def area (self):
        return self.lado ** 2

def area (poligono):
    return poligono.area()
    


mi_triangulo = (triangulo(7,2))
mi_rectangulo = (rectangulo(9,2))
mi_cuadrado = (cuadrado(3))
print (area(mi_triangulo))
print (area(mi_rectangulo))
print (area(mi_cuadrado))


