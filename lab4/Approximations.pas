UNIT Approximations;
INTERFACE
  function LinearApproximation(a0, a1, x: real) : real;
  function PolynomialApproximation2(a0, a1, a2, x: real) : real;
  function PolynomialApproximation3(a0, a1, a2, a3, x: real) : real;
  function ExponentialApproximation(a0, a1, x : real) : real;
  function LogarithmicApproximation(a0, a1, x: real) : real;
  function PowerApproximation(a0, a1, x : real) : real;
IMPLEMENTATION
function LinearApproximation(a0, a1, x: real) : real;
begin
  Result:= a0*x + a1;
end;
function PolynomialApproximation2(a0, a1, a2, x: real) : real;
begin
  Result:= a0*x**2 + a1*x + a2;
end;
function PolynomialApproximation3(a0, a1, a2, a3, x: real) : real;
begin
  Result:= a0*x**3 + a1*x**2 + a2*x + a3;
end;
function ExponentialApproximation(a0, a1, x : real) : real;
begin
  Result:= a0 * E**(a1 * x);
end;
function LogarithmicApproximation(a0, a1, x: real) : real;
begin
  Result:= a0 * Ln(x) + a1;
end;
function PowerApproximation(a0, a1, x : real) : real;
begin
  Result:= a0 * x ** a1;
end;
begin
end.