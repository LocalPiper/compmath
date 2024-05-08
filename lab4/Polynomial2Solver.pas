UNIT Polynomial2Solver;
INTERFACE
    uses Summator, Calculator, Approximations, Utils, Container;
    function Solve(x, y: array of real) : Container.Container3;
IMPLEMENTATION
    function Solve(x, y: array of real) : Container.Container3;
begin
    var a, b, c: real;
    var n: integer := x.Length;

    var SX := Summate1(x, 1);
    var SY := Summate1(y, 1);
    var SX2 := Summate1(x, 2);
    var SX3 := Summate1(x, 3);
    var SX4 := Summate1(x, 4);
    var SXY := Summate2(x, y, 1, 1);
    var SX2Y := Summate2(x, y, 2, 1);

    var det := SX4 * SX2 * n + 2 * SX3 * SX2 * SX - SX2**3 - n * SX3**2 - SX4 * SX**2;
    var det1 := SX2Y * SX2 * n + SX3 * SX * SY + SX2 * SX * SXY - SY * SX2**2 - SXY * SX3 * n - SX2Y * SX**2;
    var det2 := SX4 * SXY * n + SX2Y * SX2 * SX + SX3 * SX2 * SY - SXY * SX2**2 - SX3 * SX2Y * n - SX4 * SX * SY;
    var det3 := SX4 * SX2 * SY + SX3 * SX2 * SXY + SX3 * SX * SX2Y - SX2Y * SX2**2 - SY * SX3**2 - SX4 * SXY * SX;

    a := det1 / det;
    b := det2 / det;
    c := det3 / det;

    writeln('Polynomial2 solution: ' + a + 'x^2' + ' + ' + b + 'x' + ' + ' + c);
    CalculateS3(x, y, a, b, c, PolynomialApproximation2);
    var phi := ApplyApproximation3(x, a, b, c, PolynomialApproximation2);
    var R2 := FindDetermination(phi, y);
    FindDeviation(phi, y);
    var p := new Container.Container3(R2, a, b, c);
    Result := p;
end;
begin
end.