# Name: Trang Ngo
# Date: 09/28/2022
# File Purpose: Call all the functions

import mathematics.whoami as whoami
print(whoami.getname())
import mathematics.numbers.whoami as whoami
print(whoami.getname())
import mathematics.numbers.series as series
print(series.sum(list = [1, 2, 3, 4, 5]))
import mathematics.numbers.series as series
print(series.average(list = [1, 2, 3, 4, 5]))
import mathematics.numbers.simple as simple
print(simple.addition(left = 6, right = 7))
import mathematics.numbers.simple as simple
print(simple.subtraction(left = 6, right = 7))
import mathematics.numbers.simple as simple
print(simple.multiplication(left = 6, right = 7))
import mathematics.numbers.simple as simple
print(simple.division(left = 10, right = 4))
import mathematics.geometry.whoami as whoami
print(whoami.getname())
import mathematics.geometry.rectangle as rectangle
print(rectangle.perimeter(length = 3, width = 7))
import mathematics.geometry.rectangle as rectangle
print(rectangle.area(length = 3, width = 7))
import mathematics.geometry.cube as cube
print(cube.surface_area(side=5))
import mathematics.geometry.cube as cube
print(cube.volume(side=5))
import mathematics.__init__ as init
print(init.__all__)
import mathematics.numbers.__init__ as init
print(init.__all__)
import mathematics.geometry.__init__ as init
print(init.__all__)