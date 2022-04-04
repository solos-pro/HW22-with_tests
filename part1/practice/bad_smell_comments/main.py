# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def movement(self, field, axis_x, axis_y, direction, is_flying, is_creep, speed_rate = 1):

        if is_flying and is_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flying:
            speed_rate *= 1.2
            if direction == 'UP':
                new_y = axis_y + speed_rate
                new_x = axis_x
            elif direction == 'DOWN':
                new_y = axis_y - speed_rate
                new_x = axis_x
            elif direction == 'LEFT':
                new_y = axis_y
                new_x = axis_x - speed_rate
            elif direction == 'RIGHT':
                new_y = axis_y
                new_x = axis_x + speed_rate
        if is_creep:
            speed_rate *= 0.5
            if direction == 'UP':
                new_y = axis_y + speed_rate
                new_x = axis_x
            elif direction == 'DOWN':
                new_y = axis_y - speed_rate
                new_x = axis_x
            elif direction == 'LEFT':
                new_y = axis_y
                new_x = axis_x - speed_rate
            elif direction == 'RIGHT':
                new_y = axis_y
                new_x = axis_x + speed_rate

            field.set_unit(x=new_x, y=new_y, unit=self)

