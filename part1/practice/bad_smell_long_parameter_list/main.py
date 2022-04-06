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
    def __init__(self, x=0, y=0):
        self._speed = 1
        self.x = x
        self.y = y

    def _get_speed(self, is_fly=None, crawl=None):
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')
        elif is_fly:
            self._speed = 1.2
        elif crawl:
            self._speed = 0.5
        else:
            self._speed = 1
        return self._speed

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        if direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        if direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        if direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)




