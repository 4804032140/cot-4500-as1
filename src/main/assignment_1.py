import math

def float64(bitString):
    s = int(bitString[0])
    c = 0
    for i in range(1, 12):
        c += int(bitString[i]) * (2**(11-i))
    f = 0
    for i in range(12, 63):
        # print(bitString[i])
        f += int(bitString[i]) * (0.5)**(i-11)
    output = (-1)**s * 2**(c-1023.0) * (1.0+f)
    return output


# Assumes series is the one giving in question 5 at x = 1
def infinate_series_prescion(precision):
    precision = precision**-1
    precision = precision**(1/3)
    precision = precision - 1
    return math.ceil(precision)


def bisection_method(left: float, right: float, given_function: str):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = 10**-4
    diff: float = right - left


    # max_iterations = 20
    iteration_counter = 0
    while (diff >= tolerance):
        iteration_counter += 1
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break
        x = left
        evaluated_left_point = eval(given_function)

        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point

        diff = abs(right - left)
        # OPTIONAL: you can see how the root finding for bisection works per iteration
        # print(mid_point)
    return iteration_counter

def custom_derivative(value):
    return (3 * value * value) + 8 * value

def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0
    # finds f
    x = initial_approximation
    f = eval(sequence)
    # finds f'
    f_prime = custom_derivative(initial_approximation)

    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)
        # finds f'
        f_prime = custom_derivative(initial_approximation)
        # division operation
        approximation = f / f_prime
        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
    return iteration_counter

if __name__ == "__main__":
    bitString = "0100000001111110101110010000000000000000000000000000000000000000"
    bitNum = float64(bitString)
    print('{0:.4f}'.format(bitNum))
    print()
    print('{0:.1f}'.format(math.floor(bitNum)))
    print()
    roundedBitNum = float('{0:.1f}'.format(math.floor(bitNum + 0.5)))
    print(roundedBitNum)
    print()
    print(abs(bitNum - roundedBitNum))
    print(abs(bitNum - roundedBitNum) / abs(bitNum))
    print()

    precision = 10**-4
    numSeriesIteration = infinate_series_prescion(10**-4)
    print(numSeriesIteration)
    print()

    function_string = "x**3 + (4*(x**2)) - 10"
    left = -4
    right = 7
    bisectionIterations = bisection_method(left, right, function_string)
    print(bisectionIterations)
    print()
    newtonIterations = newton_raphson(right, 10**-4, function_string)
    print(newtonIterations)

    #function_string = "x**3 - x**2 + 4"
    #quizNewtonQ = newton_raphson(1, 0.001, function_string)
    #print(quizNewtonQ)
