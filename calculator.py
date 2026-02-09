import tkinter as tk
import math

def sanitize_expression(expr: str) -> str:
    expr = expr.replace('√(', 'sqrt(')
    expr = expr.replace('√', 'sqrt(')
    expr = expr.replace('x²', '**2')
    expr = expr.replace('x^y', '**')
    return expr

SAFE_GLOBALS = {'__builtins__': None}
SAFE_FUNCS = {
    'sqrt': math.sqrt,
    'sin': lambda x: math.sin(math.radians(x)),
    'cos': lambda x: math.cos(math.radians(x)),
    'tan': lambda x: math.tan(math.radians(x)),
    'cot': lambda x: (1.0 / math.tan(math.radians(x))) if math.tan(math.radians(x)) != 0 else float('inf'),
    'Log': lambda x: math.log10(x),
    'log10': lambda x: math.log10(x),
    'pi': math.pi,
    'e': math.e,
}

def safe_eval(expr: str):
    expr = sanitize_expression(expr)
    try:
        value = eval(expr, SAFE_GLOBALS, SAFE_FUNCS)
        return value, None
    except Exception as e:
        return None, str(e)

class LightCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("پروژه کارگاه کامپیوتر")
        self.resizable(False, False)
        self.expr = ''
        self.last_result = False
        self.geometry("840x520")
        self._create_widgets()
        self._bind_keys()

    def _create_widgets(self):
        self.configure(bg='#f0f0f0')
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self, textvariable=self.display_var, font=('Arial', 28), justify='right',
            bg='#ffffff', fg='#000000', insertbackground='black'
        )
        self.display.grid(row=0, column=0, columnspan=6, padx=20, pady=(15,10), ipady=15)
        self.display_var.set('0')
        buttons = [
            ('C', 1, 0, '#ff5555', 1), ('⌫', 1, 1, '#ff6666', 1), ('(', 1, 2, '#5555ff', 1),
            (')', 1, 3, '#5555ff', 1), ('+/-', 1, 4, '#5555ff', 1), ('Log', 1, 5, '#5555ff', 1),
            ('7', 2, 0, '#d9d9d9', 1), ('8', 2, 1, '#d9d9d9', 1), ('9', 2, 2, '#d9d9d9', 1),
            ('-', 2, 3, '#ffaa00', 1), ('+', 2, 4, '#ffaa00', 1), ('sin', 2, 5, '#ffaa00', 1),
            ('4', 3, 0, '#d9d9d9', 1), ('5', 3, 1, '#d9d9d9', 1), ('6', 3, 2, '#d9d9d9', 1),
            ('*', 3, 3, '#ffaa00', 1), ('/', 3, 4, '#ffaa00', 1), ('cos', 3, 5, '#ffaa00', 1),
            ('1', 4, 0, '#d9d9d9', 1), ('2', 4, 1, '#d9d9d9', 1), ('3', 4, 2, '#d9d9d9', 1),
            ('x²', 4, 3, '#ffaa00', 1), ('x^y', 4, 4, '#ffaa00', 1), ('tan', 4, 5, '#ffaa00', 1),
            ('0', 5, 0, '#d9d9d9', 2), ('.', 5, 2, '#d9d9d9', 1), ('=', 5, 3, '#55ff55', 1),
            ('√', 5, 4, '#ffaa00', 1), ('cot', 5, 5, '#ffaa00', 1)
        ]

        self.buttons = []
        for (text, r, c, color, colspan) in buttons:
            btn = tk.Button(
                self,
                text=text,
                bg=color,
                fg='#000000',
                font=('Arial', 16),
                relief='raised',
                activebackground='#cccccc',
                activeforeground='#000000',
                command=lambda t=text: self._click(t)
            )
            btn.grid(row=r, column=c, columnspan=colspan, sticky='nsew', padx=7, pady=7, ipadx=10, ipady=12)
            self.buttons.append(btn)

        for i in range(6):
            self.grid_columnconfigure(i, weight=1)

    def _bind_keys(self):
        self.bind('<Return>', lambda e: self._click('='))
        self.bind('<BackSpace>', lambda e: self._click('⌫'))
        self.bind('<Escape>', lambda e: self._click('C'))
        for k in '0123456789.+-*/()':
            self.bind(k, lambda e, ch=k: self._click(ch))
        self.bind('<s>', lambda e: self._click('sin'))   
        self.bind('<c>', lambda e: self._click('cos'))   
        self.bind('<t>', lambda e: self._click('tan'))   
        self.bind('<l>', lambda e: self._click('Log'))   
        self.bind('<o>', lambda e: self._click('cot'))   

    def _click(self, key):
        if key.isdigit() or key in '+-*/.()':
            if self.last_result and key.isdigit():
                self.expr = ''
                self.last_result = False
            self.expr += key
            self.display_var.set(self.expr if self.expr else '0')
            return

        if key == 'C':
            self.expr = ''
            self.display_var.set('0')
            self.last_result = False
            return

        if key == '⌫':
            self.expr = self.expr[:-1]
            self.display_var.set(self.expr if self.expr else '0')
            return

        if key == '+/-':
            if self.expr.startswith('-'):
                self.expr = self.expr[1:]
            else:
                self.expr = '-' + self.expr if self.expr else '-'
            self.display_var.set(self.expr if self.expr else '0')
            return

        if key == '√':
            self.expr += 'sqrt('
            self.display_var.set(self.expr)
            return

        if key == 'x²':
            self.expr += '**2'
            self.display_var.set(self.expr)
            return

        if key == 'x^y':
            self.expr += '**'
            self.display_var.set(self.expr)
            return

        if key in ('sin', 'cos', 'tan', 'cot'):
            self.expr += key + '('
            self.display_var.set(self.expr)
            return

        if key == 'Log':
            self.expr += 'Log('
            self.display_var.set(self.expr)
            return

        if key == '=':
            if not self.expr:
                self.display_var.set('0')
                return

            expr_to_eval = self.expr
            open_parens = expr_to_eval.count('(')
            close_parens = expr_to_eval.count(')')
            if open_parens > close_parens:
                expr_to_eval += ')' * (open_parens - close_parens)

            value, err = safe_eval(expr_to_eval)
            if err is not None:
                self.display_var.set('Error')
                self.expr = ''
                self.last_result = False
            else:
                if isinstance(value, float) and value.is_integer():
                    value = int(value)
                self.display_var.set(str(value))
                self.expr = str(value)
                self.last_result = True
            return

        self.expr += str(key)
        self.display_var.set(self.expr)

if __name__ == '__main__':
    app = LightCalculator()
    app.mainloop()