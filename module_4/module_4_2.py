def test_function():
    def inner_function():
        print(f'Я в области видимости функции {test_function}')
    inner_function()


test_function()
# inner_function() - данная функция находится в зоне видимости лишь функции test_function и не может быть вызвана из global пространства имён