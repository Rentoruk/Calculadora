import tkinter as tk
from tkinter import messagebox


class calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')


        #Atributos para la clase
        self.expresion = ''
        # Caja de texto (input)
        self.entrada = None
        #StringVar lo utilizamos para actualizar el input
        self.entrada_texto = tk.StringVar()
        #Creamos un metodo para los componentes
        self._creacion_componentes()

    def _creacion_componentes(self):
        #Primer frame
        entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)
        #Agregamos el componente de caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial',18,'bold'),
                           textvariable=self.entrada_texto, width=30, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10)

        #Segundo frame para los botones de la calculadora
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()

        #Primer renglon
        boton_limpiar = tk.Button(botones_frame,text='C', width=39, height=4,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=self._eventolimpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        #Boton de division
        boton_dividir = tk.Button(botones_frame, text='/', width=15, height=4,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._eventoclick('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        #Boton del numero 7
        boton_seven = tk.Button(botones_frame, text='7', width=12, height=4,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._eventoclick('7'))
        boton_seven.grid(row=1, column=0, padx=1, pady=1)
        #Boton del numero 8
        boton_eight = tk.Button(botones_frame, text='8', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('8'))
        boton_eight.grid(row=1, column=1, padx=1, pady=1)
        # Boton del numero 9
        boton_nine = tk.Button(botones_frame, text='9', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('9'))
        boton_nine.grid(row=1, column=2, padx=1, pady=1)
        #Boton de multiplicacion
        boton_multi = tk.Button(botones_frame, text='*', width=15, height=4,
                               bd=0, bg='#eee', cursor='hand2',
                               command=lambda: self._eventoclick('*'))
        boton_multi.grid(row=1, column=3, padx=1, pady=1)
        # Boton del numero 4
        boton_four = tk.Button(botones_frame, text='4', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('4'))
        boton_four.grid(row=2, column=0, padx=1, pady=1)
        # Boton del numero 5
        boton_five = tk.Button(botones_frame, text='5', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('5'))
        boton_five.grid(row=2, column=1, padx=1, pady=1)
        # Boton del numero 6
        boton_six = tk.Button(botones_frame, text='6', width=12, height=4,
                               bd=0, bg='#eee', cursor='hand2',
                               command=lambda: self._eventoclick('6'))
        boton_six.grid(row=2, column=2, padx=1, pady=1)
        # Boton de resta
        boton_rest = tk.Button(botones_frame, text='-', width=15, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('-'))
        boton_rest.grid(row=2, column=3, padx=1, pady=1)
        # Boton del numero 1
        boton_one = tk.Button(botones_frame, text='1', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('1'))
        boton_one.grid(row=3, column=0, padx=1, pady=1)
        # Boton del numero 2
        boton_two = tk.Button(botones_frame, text='2', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('2'))
        boton_two.grid(row=3, column=1, padx=1, pady=1)
        # Boton del numero 3
        boton_trhee = tk.Button(botones_frame, text='3', width=12, height=4,
                               bd=0, bg='#eee', cursor='hand2',
                               command=lambda: self._eventoclick('3'))
        boton_trhee.grid(row=3, column=2, padx=1, pady=1)
        # Boton dse suma
        boton_suma = tk.Button(botones_frame, text='+', width=15, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)
        boton_one = tk.Button(botones_frame, text='1', width=12, height=4,
                              bd=0, bg='#eee', cursor='hand2',
                              command=lambda: self._eventoclick('1'))
        boton_one.grid(row=3, column=0, padx=1, pady=1)
        # Boton del numero 0
        boton_cero = tk.Button(botones_frame, text='0', width=26, height=4,
                              bd=0, bg='#eee', cursor='hand2',
                              command=lambda: self._eventoclick('0'))
        boton_cero.grid(row=4, column=0,columnspan=2, padx=1, pady=1)
        # Boton del punto decimal
        boton_punto = tk.Button(botones_frame, text='.', width=12, height=4,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._eventoclick('.'))
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        # Boton del igual
        boton_igual = tk.Button(botones_frame, text='=', width=15, height=4,
                               bd=0, bg='#eee', cursor='hand2',
                               command=self._eventoevaluar)
        boton_igual.grid(row=4, column=3, padx=1, pady=1)

    def _eventoevaluar(self):
        #Eval evaluala expresion str como una expresion aritmetica
        try:
            if self.expresion:
                resultado=str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error',f'Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion=''

    def _eventolimpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
    def _eventoclick(self, elemento):
        #concatenamos el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)



if __name__ == '__main__':
    Calculadora = calculadora()
    Calculadora.mainloop()
