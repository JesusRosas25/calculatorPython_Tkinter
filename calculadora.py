import tkinter as tk
from tkinter import Tk, ttk, EW
import os
from tkinter import messagebox

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
absolute_image_path = os.path.join(absolute_folder_path, 'calculadora.ico')
class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x390')
        self.title('Calculadora')
        self.resizable(0,0)
        self.iconbitmap(absolute_image_path)
        # Atributo de clase
        self.expresion = ''
        # caja de texto (input)
        self.entrada = None
        # StringVar lo utilizamos para obtener el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=300, height=55, bg='grey')
        entrada_frame.pack(side=tk.TOP)    
        # CAja de texto
        self.screem = tk.Entry(entrada_frame, width=22, font=('arial', 18, 'bold'), textvariable=self.entrada_texto, justify='right')
        self.screem.grid(row=0, column=0,ipady=5, sticky=tk.NSEW )
        # Creamos otro frame para los botones
        botones_frame = tk.Frame(self, width=300, height=340, bg='grey')
        botones_frame.pack()       
        boton_c = tk.Button(botones_frame, text='C', width=32, height=4, bd=0, bg='#eee', command=self.evento_limpiar)
        boton_c.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
    
        boton_dividir = tk.Button(botones_frame, text='/', width=8, height=4, bd=0, bg='#eee', command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, columnspan=1, padx=1, pady=1)
        
        boton_7 = tk.Button(botones_frame, text='7', width=10, height=4, bd=0, bg='white', command=lambda: self._evento_click(7)).grid(row=2, column=0, columnspan=1, padx=1, pady=1)
        boton_8 = tk.Button(botones_frame, text='8', width=10, height=4, bd=0, bg='white', command=lambda: self._evento_click(8) )
        boton_8.grid(row=2, column=1, columnspan=1, padx=1, pady=1)
        boton_9 = tk.Button(botones_frame, text='9', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(9))
        boton_9.grid(row=2, column=2, columnspan=1, padx=1, pady=1)
        boton_multiplicar = tk.Button(botones_frame, text='*', width=8, height=4, bd=0, bg='#eee', command=lambda:self._evento_click('*'))
        boton_multiplicar.grid(row=2, column=3, padx=1, pady=1)
        boton_4 = tk.Button(botones_frame, text='4', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(4))
        boton_4.grid(row=3, column=0, columnspan=1, padx=1, pady=1)
        boton_5 = tk.Button(botones_frame, text='5', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(5))
        boton_5.grid(row=3, column=1, columnspan=1, padx=1, pady=1)
        boton_6 = tk.Button(botones_frame, text='6', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(6))
        boton_6.grid(row=3, column=2, columnspan=1, padx=1, pady=1)
        boton_restar = tk.Button(botones_frame, text='-', width=8, height=4, bd=0, bg='#eee', command=lambda:self._evento_click('-'))
        boton_restar.grid(row=3, column=3, columnspan=1, padx=1, pady=1)
        boton_1 = tk.Button(botones_frame, text='1', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(1))
        boton_1.grid(row=4, column=0, columnspan=1, padx=1, pady=1)
        boton_2 = tk.Button(botones_frame, text='2', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(2))
        boton_2.grid(row=4, column=1, columnspan=1, padx=1, pady=1)
        boton_3 = tk.Button(botones_frame, text='3', width=10, height=4, bd=0, bg='white', command=lambda:self._evento_click(3))
        boton_3.grid(row=4, column=2, columnspan=1, padx=1, pady=1)
        boton_sumar = tk.Button(botones_frame, text='+', width=8, height=4, bd=0, bg='#eee', command=lambda:self._evento_click('+'))
        boton_sumar.grid(row=4, column=3, columnspan=1, padx=1, pady=1)
        boton_0 = tk.Button(botones_frame, text='0', width=21, height=4, bd=0, bg='white', command=lambda:self._evento_click(0))
        boton_0.grid(row=5, column=0, columnspan=2, padx=1, pady=1)
        boton_punto = tk.Button(botones_frame, text='.', width=10, height=4, bd=0, bg='#eee', command=lambda:self._evento_click('.'))
        boton_punto.grid(row=5, column=2, columnspan=1, padx=1, pady=1)
        boton_igual = tk.Button(botones_frame, text='=', width=8, height=4, bd=0, bg='#eee', command=self._evento_evaluar)
        boton_igual.grid(row=5, column=3, columnspan=1, padx=1, pady=1)
    def evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
        
    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)
    def _evento_evaluar(self): 
        # eval evalua la expresion str como una expresion aritmetica
        try:
            resulatdo = str(eval(self.expresion))
            self.entrada_texto.set(resulatdo)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:    
            self.expresion = ''
if __name__ == '__main__':
    nueva_calculadora = Calculadora()
    nueva_calculadora.mainloop()

# def crear_calculator():
#     calculator = ttk.Frame(calculadora)
#     calculator.add(screem)
#     crear_pantalla(screem)
