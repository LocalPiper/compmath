unit LinearSolver;

interface

uses Summator, Calculator, Approximations, Utils, Container;

function Solve(x, y: array of real): Container.Container2;
implementation

function Solve(x, y: array of real): Container.Container2;
begin
  var a, b: real;
  var n: integer := x.Length;
  FindCorellation(x, y);
  
  var SX := Summate1(x, 1);
  var SY := Summate1(y, 1);
  var SX2 := Summate1(x, 2);
  var SXY := Summate2(x, y, 1, 1);
  
  var det := SX2 * n - SX ** 2;
  var det1 := SXY * n - SX * SY;
  var det2 := SX2 * SY - SX * SXY;
  
  a := det1 / det;
  b := det2 / det;
  
  writeln('Linear solution: ' + a + 'x' + ' + ' + b);
  CalculateS2(x, y, a, b, LinearApproximation);
  var phi := ApplyApproximation2(x, a, b, LinearApproximation);
  FindDeviation(phi, y);
  var R2 := FindDetermination(phi, y);
  var p : Container.Container2 := new Container.Container2(R2, a, b);
  
  Result := p;
end;

begin
end. 