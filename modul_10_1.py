import time
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open (file_name, mode='a', encoding='utf-8') as file:
        for i in range (word_count):
            file.write (f"Как прекрасен этот мир!- № {i + 1}\n")
            time.sleep (0.1)
        print (f'Завершилась запись в файл {file_name}')


time_start = datetime.now ()
write_words (10, 'example1.txt')
write_words (30, 'example2.txt')
write_words (200, 'example3.txt')
write_words (100, 'example4.txt')
time_end = datetime.now ()
time_res1 = time_end - time_start
print ()
print (f'Время срабатывания функций:{time_res1}')
print ()
time_start = datetime.now ()

fl1 = Thread (target=write_words, args=(10, 'example5.txt'))
fl2 = Thread (target=write_words, args=(30, 'example6.txt'))
fl3 = Thread (target=write_words, args=(200, 'example7.txt'))
fl4 = Thread (target=write_words, args=(100, 'example8.txt'))
fl1.start ()
fl2.start ()
fl3.start ()
fl4.start ()
fl1.join ()
fl2.join ()
fl3.join ()
fl4.join ()
time_end = datetime.now ()
time_res2 = time_end - time_start
print ()
print (f'Время срабатывания потока:{time_res2}')
print ()
print (f'Поток срабатывает быстрее функций на {time_res1 - time_res2}')
