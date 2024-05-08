UNIT Utils;
INTERFACE
    procedure PrintVector(x,y : array of real);
    function ApplyApproximation2(x : array of real; a, b : real; F : (real, real, real)->real) : array of real;
    function ApplyApproximation3(x : array of real; a, b, c : real; F : (real, real, real, real)->real) : array of real;
    function ApplyApproximation4(x : array of real; a, b, c, d : real; F : (real, real, real, real, real)->real) : array of real;
    function NormalizeVector(x : array of real; nx : real) : array of real;
    function SubtractVector(x, y : array of real) : array of real;
IMPLEMENTATION
procedure PrintVector(x,y : array of real);
begin
    for var i := 0 to x.Length - 1 do
        writeln('(' + x[i] + ', ' + y[i] + ')');
end;
function ApplyApproximation2(x : array of real; a, b : real; F : (real, real, real)->real) : array of real;
begin
    var phi : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do
        phi[i] := F(a,b,x[i]);
    Result := phi;
end;
function ApplyApproximation3(x : array of real; a, b, c : real; F : (real, real, real, real)->real) : array of real;
begin
    var phi : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do
        phi[i] := F(a,b,c,x[i]);
    Result := phi;
end;
function ApplyApproximation4(x : array of real; a, b, c, d : real; F : (real, real, real, real, real)->real) : array of real;
begin
    var phi : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do
        phi[i] := F(a,b,c,d,x[i]);
    Result := phi;
end;
function NormalizeVector(x : array of real; nx : real) : array of real;
begin
    var xi : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do
        xi[i] := x[i] - nx;
    Result := xi;
end;
function SubtractVector(x, y : array of real) : array of real;
begin
    var xi : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do
        xi[i] := x[i] - y[i];
    Result := xi;
end;
begin
end.