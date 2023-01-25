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
import math
class poligono:
    def __init__(self, tipo, base,altura=-1):
        self.tipo=tipo
        self.base = base
        self.altura = altura
    def area (self):
        if self.tipo == "triangulo":
            return self.base * self.altura/2
        elif self.tipo == "rectangulo":
            return self.base * self.altura
        else:
            return self.base ** 2
    def perimetro (self):
        if self.tipo == "triangulo":
            return print("faltan datos para calcular el perímetro")
        elif self.tipo == "rectangulo":
            return (self.base + self.altura) * 2
        else:
            return self.base * 4


triangulo = poligono("triangulo",3.2,7)
rectangulo = poligono("rectangulo",7.23,2)
cuadrado = poligono("cuadrado",7)

print(triangulo.area())
print(rectangulo.area())
print(cuadrado.area())

print(triangulo.perimetro())
print(rectangulo.perimetro())
print(cuadrado.perimetro())



