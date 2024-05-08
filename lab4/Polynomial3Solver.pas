UNIT Polynomial3Solver;
INTERFACE
    uses Summator, Calculator, Approximations, Utils, Container;
    function Solve(x, y: array of real) : Container.Container4;
IMPLEMENTATION
    function Solve(x, y: array of real) : Container.Container4;
begin
    var a, b, c, d: real;
    var n: integer := x.Length;

    var SX := Summate1(x, 1);
    var SY := Summate1(y, 1);
    var SX2 := Summate1(x, 2);
    var SX3 := Summate1(x, 3);
    var SX4 := Summate1(x, 4);
    var SX5 := Summate1(x, 5);
    var SX6 := Summate1(x, 6);
    var SXY := Summate2(x, y, 1, 1);
    var SX2Y := Summate2(x, y, 2, 1);
    var SX3Y := Summate2(x, y, 3, 1);

    var M : array [,] of real := ((SX6, SX5, SX4, SX3, SX3Y), (SX5, SX4, SX3, SX2, SX2Y), (SX4, SX3, SX2, SX, SXY), (SX3, SX2, SX, n, SY));

    for var i := 0 to 3 do begin
        for var j := i + 1 to  3 do begin
            var ratio := M[j, i]/M[i, i];
            for var k := 0 to 4 do begin
                M[j, k] := M[j, k] - ratio * M[i, k];
            end;
        end;
    end;

    var XA : array of real := new real[4];
    XA[3] := M[3, 4]/M[3, 3];
    for var i := 2 downto 0 do begin
        XA[i] := M[i, 4];
        for var j := i+1 to 3 do
            XA[i] := XA[i] - M[i, j] * XA[j];
        XA[i] := XA[i] / M[i, i];
    end;

    a := XA[0];
    b := XA[1];
    c := XA[2];
    d := XA[3];

    writeln('Polynomial3 solution: ' + a + 'x^3' + ' + ' + b + 'x^2' + ' + ' + c + 'x' + ' + ' + d);
    CalculateS4(x, y, a, b, c, d, PolynomialApproximation3);
    var phi := ApplyApproximation4(x, a, b, c, d, PolynomialApproximation3);
    var R2 := FindDetermination(phi, y);
    FindDeviation(phi, y);
    var p := new Container.Container4(R2, a, b, c, d);
    Result := p;
end;

begin
end.