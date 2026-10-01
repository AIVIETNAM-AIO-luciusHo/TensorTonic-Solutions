def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
   x =float(x0)
   for _ in range(steps):
       #Calculator derivative 
     grad=2.0*a*x+b
       #gradient descent 
     x=x-lr*grad
   return float(x)