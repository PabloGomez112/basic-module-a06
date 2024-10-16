import re
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog as fd

window = Tk()

MAX_ARGUMENTS = 3
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 300

WINDOW_ANALYZE_WIDTH = 450
WINDOW_ANALYZE_HEIGHT = 300

ELEMENTS_PADDING = 10

OUTPUT_FILE_EXTENSION = '.txt'
EMPTY_STRING = ''

WRITE_MODE = 'w'

path_to_file = EMPTY_STRING
generated_file_name = StringVar()

regular_match_args = r'\$(\d{1,2})'
regular_match_keywords = r'^\S+'

argsRegex = re.compile(regular_match_args)
keywordsRegex = re.compile(regular_match_keywords)

keywords = {'SUMA': {'ALUC': '010', 'MC': '01'},
            'RESTA': {'ALUC': '110', 'MC': '01'},
            'AND': {'ALUC': '000', 'MC': '01'},
            'MENORQ': {'ALUC': '111', 'MC': '01'},
            'LEER': {'ALUC': '000', 'MC': '10'},
            '*MOVER': {'ALUC': '000', 'MC': '10'}}


def generate_code(aluc: str, *args) -> str:
    alucode = keywords[aluc]['ALUC']
    mc = keywords[aluc]['MC']

    rs = bin(int(args[0][0]))[2:].zfill(5)

    if aluc != 'LEER':
        rt = bin(int(args[0][1]))[2:].zfill(5)
        rd = bin(int(args[0][2]))[2:].zfill(5)
    else:
        rt = bin(0)[2:].zfill(5)
        rd = bin(0)[2:].zfill(5)

    if len(args) > MAX_ARGUMENTS:
        instruction = None
    else:
        instruction = str(mc) + str(rt) + alucode + str(rd) + str(rs)

    return instruction


def generate_machine_code(path) -> bool:
    global generated_file_name

    if path == EMPTY_STRING or generated_file_name.get() == EMPTY_STRING:
        return False
    else:
        with open(path) as assemblerFile:
            lines = assemblerFile.readlines()
            generate_file = open(str(generated_file_name.get() + OUTPUT_FILE_EXTENSION), WRITE_MODE)

            for a in lines:
                if a != '\n':
                    actual_keyword = keywordsRegex.search(a)
                    actual_args = argsRegex.findall(a)

                    try:
                        generate_file.write(generate_code(actual_keyword.group(), actual_args) + "\n")
                    except NameError:
                        print(NameError)
                        continue

            generate_file.close()
            return True


def handle_button_select_file():
    global path_to_file

    filetypes = (('Text files', '.txt'), ('All files', '.*'))

    path_to_file = fd.askopenfilename(title='Selecciona el archivo ASM', initialdir='.', filetypes=filetypes)
    print(path_to_file)


def handle_button_generate_code():
    if generate_machine_code(path_to_file):
        tkinter.messagebox.showinfo(title='Operacion exitosa', message='Se ha generado el archivo correctamente')
    else:
        tkinter.messagebox.showerror(title='Error al crear el archivo', message='Asegurese haber seleccionado un '
                                                                                'archivo assembler y haber otorgado '
                                                                                'un nombre al archivo que se generara')


def handle_button_analyze():
    global path_to_file

    def create_analyze_window():

        window_analyze = Toplevel(window)

        text_area = Text(window_analyze)
        scrollbar = Scrollbar(window_analyze)

        scrollbar.pack(side=RIGHT, fill=tkinter.Y)
        text_area.pack(side=LEFT, fill=tkinter.Y)
        scrollbar.config(command=text_area.yview)
        text_area.config(yscrollcommand=scrollbar.set)

        with open(path_to_file, encoding='utf-8') as file:
            lines = file.readlines()

            for line in lines:
                text_area.insert(tkinter.END, line)

        text_area.config(state='disabled')

        window_analyze.title('Analizar codigo')
        window_analyze.geometry(f'{WINDOW_ANALYZE_WIDTH}x{WINDOW_ANALYZE_HEIGHT}+{WINDOW_WIDTH + ELEMENTS_PADDING}+20')
        window_analyze.iconbitmap('chocoicono.ico')
        window_analyze.mainloop()

    if path_to_file != EMPTY_STRING:
        create_analyze_window()
    else:
        tkinter.messagebox.showerror(title='Ningun archivo seleccionado', message='Selecciona un archivo Assembler')


def create_main_window():
    global generated_file_name

    generated_file_name = tkinter.StringVar()

    select_file_button = Button(window, text='Seleccionar archivo ASM', command=handle_button_select_file)
    select_file_button.pack(pady=ELEMENTS_PADDING)
    label_input_name = Label(text='Nombre del archivo a generar ')
    label_input_name.pack(pady=ELEMENTS_PADDING)
    entry_input_name = Entry(textvariable=generated_file_name)
    entry_input_name.pack(pady=ELEMENTS_PADDING)
    generate_code_button = Button(window, text='Generar codigo maquina', command=handle_button_generate_code)
    generate_code_button.pack(pady=ELEMENTS_PADDING)

    analyze_button = Button(window, text='Analizar', command=handle_button_analyze)
    analyze_button.pack(pady=ELEMENTS_PADDING)

    window.title('Generador de codigo maquina')
    window.resizable(False, False)
    window.iconbitmap('chocoicono.ico')

    window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+10+20')
    window.mainloop()


if __name__ == '__main__':
    create_main_window()
