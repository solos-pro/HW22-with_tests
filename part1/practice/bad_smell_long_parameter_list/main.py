# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self):
        self._speed = 1
        self.new_x = 0
        self.new_y = 0

    def get_speed(self, is_fly, crawl):
        if is_fly:
            self._speed = 1.2
        elif crawl:
            self._speed = 0.5
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        else:
            self._speed = 1
        return self._speed

    def move(self, field, x_coord, y_coord, direction):

        if direction == 'UP':
            self.new_y = y_coord + self._speed
            self.new_x = x_coord
        elif direction == 'DOWN':
            self.new_y = y_coord - self._speed
            self.new_x = x_coord
        elif direction == 'LEFT':
            self.new_y = y_coord
            self.new_x = x_coord - self._speed
        elif direction == 'RIGTH':
            self.new_y = y_coord
            self.new_x = x_coord + self._speed


            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
