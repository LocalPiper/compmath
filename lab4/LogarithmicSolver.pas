UNIT LogarithmicSolver;
INTERFACE
    uses Summator, Preprocessor, Calculator, Approximations, Utils, Container, ArraySanitizer;
    function Solve(x, y: array of real) : Container.Container2;
IMPLEMENTATION
function Solve(x, y: array of real) : Container.Container2;
begin
    var sanitized := SanitizeForLn(x,y, 0);
    var newX := Preprocess(sanitized.x);
    var newY := sanitized.y;

    var A, B: real;
    var n : integer := newX.Length;

    var SX := Summate1(newX, 1);
    var SY := Summate1(newY, 1);
    var SX2 := Summate1(newX, 2);
    var SXY := Summate2(newX, newY, 1, 1);

    var det := SX2 * n - SX**2;
    var det1 := SXY * n - SX * SY;
    var det2 := SX2 * SY - SX * SXY;

    A := det <> 0? det1/det : 0;
    B := det <> 0? det2/det : 0;

    writeln('Logarithmic solution: ' + A + 'ln x' + ' + ' + B);
    CalculateS2(x, y, a, b, LogarithmicApproximation);
    var phi := ApplyApproximation2(x, a, b, LogarithmicApproximation);
    var R2 := FindDetermination(phi, y);
    FindDeviation(phi, y);
    var p := new Container.Container2(R2, a, b);
    Result := p;
end;

begin
end.