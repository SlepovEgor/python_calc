class engine():

    arg1 = ''
    arg2 = ''
    op = ''
    result = ''

    def get_result(self):
        return str(self.result)

    def _set_result(self, result):
        self.result = str(result)

    def set_arg(self, arg):
        if self.op == '':
            self._set_arg1(arg)
        else:
            self._set_arg2(arg)

    def _set_arg1(self, arg):
        self.arg1 = str(arg)

    def _set_arg2(self, arg):
        self.arg2 = str(arg)

    def set_op(self, op):
        self.op = str(op)

    def do_math(self):
        result = 'Math undone'
        if (self.arg1 != '' and self.arg2 != '' and self.op != ''):
            if self.op == '+':
                result = str(int(self.arg1) + int(self.arg2))
            elif self.op == '-':
                result = str(int(self.arg1) - int(self.arg2))
            else:
                pass
            self._set_result(result)
            self.set_arg('')
            self.set_op('')
            self.set_arg(self.result)

    def clear(self):
        self._set_arg1('')
        self._set_arg2('')
        self.set_op('')
        self._set_result('')
