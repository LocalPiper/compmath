UNIT Summator;
INTERFACE
  function Summate1(x : array of real; p : integer) : real;
  function Summate2(x, y : array of real; p1, p2 : integer) : real;
IMPLEMENTATION
function Summate1(x : array of real; p : integer) : real;
begin
  var s: real := 0;
  for var i:= 0 to x.Length - 1 do
    s += x[i]**p;
  Result:= s;
end;
function Summate2(x, y : array of real; p1, p2 : integer) : real;
begin
  var s: real := 0;
  for var i:= 0 to x.Length - 1 do
    s += (x[i]**p1) * (y[i]**p2);
  Result:= s;
end;
begin
end.
