UNIT Preprocessor;
INTERFACE
    function Preprocess(x: array of real) : array of real;
IMPLEMENTATION
function Preprocess(x: array of real) : array of real;
begin
    var xi : array of real := new real[x.Length];
    for var i := 0 to x.Length - 1 do
        xi[i] := Ln(x[i]);
    Result := xi;
end;
begin
end.