UNIT Calculator;
INTERFACE
    uses Utils, Summator;
    procedure CalculateS2(x, y : array of real; a, b : real; F : (real, real, real) -> real);
    procedure CalculateS3(x, y : array of real; a, b, c : real; F : (real, real, real, real) -> real);
    procedure CalculateS4(x, y : array of real; a, b, c, d : real; F : (real, real, real, real, real) -> real);
    procedure FindCorellation(x, y : array of real);
    procedure FindDeviation(phi, y : array of real);
    function FindDetermination(phi, y : array of real) : real;
IMPLEMENTATION
procedure CalculateS2(x, y : array of real; a, b : real; F : (real, real, real) -> real);
begin
    var sum : real := 0;
    var phi : array of real := new real[x.Length];
    var eps : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do begin
        phi[i] := F(a,b,x[i]);
        eps[i] := phi[i] - y[i];
        sum += eps[i]**2;
        end;
    writeln('S: ' + sum);
    writeln('(phi(x), eps)');
    PrintVector(phi, eps);
end;
procedure CalculateS3(x, y : array of real; a, b, c : real; F : (real, real, real, real) -> real);
begin
    var sum : real := 0;
    var phi : array of real := new real[x.Length];
    var eps : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do begin
        phi[i] := F(a,b,c,x[i]);
        eps[i] := phi[i] - y[i];
        sum += eps[i]**2;
        end;
    writeln('S: ' + sum);
    writeln('(phi(x), eps)');
    PrintVector(phi, eps);
end;
procedure CalculateS4(x, y : array of real; a, b, c, d : real; F : (real, real, real, real, real) -> real);
begin
    var sum : real := 0;
    var phi : array of real := new real[x.Length];
    var eps : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do begin
        phi[i] := F(a,b,c,d,x[i]);
        eps[i] := phi[i] - y[i];
        sum += eps[i]**2;
        end;
    writeln('S: ' + sum);
    writeln('(phi(x), eps)');
    PrintVector(phi, eps);
end;
procedure FindCorellation(x, y : array of real);
begin
    var xMid := Summate1(x, 1)/x.Length;
    var yMid := Summate1(y, 1)/y.Length;
    var xi := NormalizeVector(x, xMid);
    var yi := NormalizeVector(y, yMid);

    var SXY := Summate2(xi, yi, 1, 1);
    var SX2 := Summate1(xi, 2);
    var SY2 := Summate1(yi, 2);

    var r := SXY/Sqrt(SX2 * SY2);
    writeln('r: ' + r);
end;
procedure FindDeviation(phi, y : array of real);
begin
  var xi := SubtractVector(phi, y);
  var SX := Summate1(xi, 2);
  var dev := Sqrt(SX/phi.Length);
  writeln('Deviation: ' + dev);
end;
function FindDetermination(phi, y : array of real) : real;
begin
    var phiMid := Summate1(phi, 1)/phi.Length;
    var xi := SubtractVector(y, phi);
    var yi := NormalizeVector(y, phiMid);

    var SX2 := Summate1(xi, 2);
    var SY2 := Summate1(yi, 2);

    var R2 := SY2 <> 0? 1 - SX2/SY2 : 0;
    Result := R2;
end;
begin
end.