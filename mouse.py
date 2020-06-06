import pyautogui as a
# Узнать размер экрана
print(a.size())
# Узнать позицию курсора
print(a.position())
# Передвинуть курсор
a.moveTo(558, 88, 1)
# Выделить/Зажать ЛКМ
a.dragTo(774, 288, 1)
# Клик/Нажатие ЛКМ
a.click(clicks = 3, interval = 0.5, button = 'right')
# Изменить количество нажатий
a.click()
a.doubleClick()
a.tripleClick()
# Скролл
a.scroll(100)
# Нажатие одной клавиши
a.press('a')
# Печать фразы
a.typewrite('Hello, world!', 0.3)
# Сочитание клавиш
a.keyDown('ctrl')
a.keyDown('a')
a.keyUp('ctrl')
a.keyUp('a')
# Или
a.hotkey('ctrl', 'c')


