from translate import Translator
translator=Translator(to_lan='zh')
try:
    with open('./test.txt', mode='r') as my_file:
        text=my_file.read()
        translation=translator.translate(text)
        with open('./test_zh.txt', mode='w') as my_file1:
            my_file1.write(translation)
        print(translation)
except FileNotFoundError as err:
    print('check your file path') #end of the code


