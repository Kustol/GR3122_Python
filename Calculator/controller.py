import model_rational as ration
import model_complex as compl
import logger as log
import view

def button_click():
    choice = view.choice_number_class()
    if not choice:
        a = view.get_value()
        b = view.get_value()
        action = view.get_operation()
        ration.init(a, b)
        result = ration.do_it(action)
        view.view_data(result, 'result')
        data = f'{ration.return_x()} {action} {ration.return_y()} = {result}'
        log.logger(data)
    else:
        a = float(view.get_value())
        b = float(view.get_value())
        c = float(view.get_value())
        d = float(view.get_value())
        action = view.get_operation()
        compl.init(a, b, c, d)
        result = compl.do_it(action)
        view.view_data(result, 'result')
        data = f'{compl.return_x()} {action} {compl.return_y()} = {result}'
        log.logger(data)