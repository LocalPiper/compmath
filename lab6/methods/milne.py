from data_class.func_data import FuncData
import matplotlib.pyplot as plt

def runge_kutta(f, x0, y0, h):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        return y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
    
def correction(f, xn, yn, h):
    y_predict = runge_kutta(f, xn, yn, h)
    y_correct = yn + h/2 * (f(xn, yn) + f(xn + h, y_predict))
    return y_correct

def milne_predictor_corrector(f, c, f_s, x0, y0, h, steps, epsilon):
    

    xn = x0
    yn = y0

    y_arr = []
    y_arr.append(yn)

    print(f"N    {'x_i':<10} {'y_i':<10} {'f(x_i, y_i)':<15} {'точное решение':<15} |y_тoчн - y_i|")

    for i in range(steps):
        y_predict = runge_kutta(f, xn, yn, h)

        y_correct = correction(f, xn, yn, h)
        it = 0
        while (abs(y_correct - y_predict) > epsilon) or (it < 1000):
            y_correct = correction(f, xn, yn, h)
            it += 1
            if it >= 1000:
                print("Milne is tired and went to sleep, but you are still cringe.")
                raise ValueError

        xi = xn + h
        fi = f(xn, yn)
        fs = f_s(xn, c)
        error = abs(fs - yn)
        y_arr.append(y_correct)
        print(f"{i:<2}   {xn:<10.5f} {yn:<10.5f} {fi:<15.5f} {fs:<15.5f} {error:<15.5f}")

        xn = xi
        yn = y_correct
    
    y_predict = runge_kutta(f, xn, yn, h)
    y_correct = correction(f, xn, yn, h)
    while (abs(y_correct - y_predict) > epsilon) or (it < 1000):
        y_correct = correction(f, xn, yn, h)
        it += 1
        if it >= 1000:
                print("Milne is tired and went to sleep, but you are still cringe.")
                raise ValueError

    xi = xn + h
    fi = f(xn, yn)
    fs = f_s(xn, c)
    error = abs(fs - yn)
    
    print(f"{steps:<2}   {xn:<10.5f} {yn:<10.5f} {fi:<15.5f} {fs:<15.5f} {error:<15.5f}")

    return y_arr

def perform(fd: FuncData):
    print("\nPerforming Milne...")
    f = fd.f
    x0 = fd.a
    y0 = fd.y0
    c = fd.fc(x0, y0)
    h = fd.h
    steps = int((fd.b - fd.a) / h)
    epsilon = fd.eps

    fd.milne = milne_predictor_corrector(f, c, fd.fs, x0, y0, h, steps, epsilon)
    return fd
    

