unit ArraySanitizer;
interface
  uses CoordContainer;
  function SanitizeForLn(x, y : array of real; mode : integer) : CoordContainer.Container;
  function CheckHealth(x, y  : array of real) : boolean;
implementation
  function CheckHealth(x, y : array of real) : boolean;
  begin
    if (x.Length <> y.Length) then begin
      writeln('X and Y have different dimensions!');
      Result := false;
      exit;
    end;
    if (x.Length < 8) then begin
      writeln('X has less than 8 values!');
      Result := false;
      exit;
    end;
    if (y.Length < 8) then begin
      writeln('Y has less than 8 values!');
      Result := false;
      exit;
    end;
    Result := true;
  end;
  function SanitizeForLn(x, y : array of real; mode : integer) : CoordContainer.Container;
  begin
    var arrX, arrY: array of real;
    var count : integer := 0;
    if mode = 0 then begin
      
      for var i := 0 to x.Length - 1 do
        if x[i] > 0 then
          count += 1;
      
      arrX := new real[count];
      arrY := new real[count];
      var p := 0;
      for var i := 0 to x.Length - 1 do
        if x[i] > 0 then begin
          arrX[p] := x[i];
          arrY[p] := y[i];
          p += 1;
        end;
      Result := new CoordContainer.Container(arrX, arrY);
      end
      else if mode = 1 then begin
        for var i := 0 to x.Length - 1 do
        if y[i] > 0 then
          count += 1;
      
      arrX := new real[count];
      arrY := new real[count];
      var p := 0;
      for var i := 0 to x.Length - 1 do
        if y[i] > 0 then begin
          arrX[p] := x[i];
          arrY[p] := y[i];
          p += 1;
        end;
      Result := new CoordContainer.Container(arrX, arrY);
      end
      else begin
        for var i := 0 to x.Length - 1 do
        if (y[i] > 0) and (x[i] > 0) then
          count += 1;
      
      arrX := new real[count];
      arrY := new real[count];
      var p := 0;
      for var i := 0 to x.Length - 1 do
        if (y[i] > 0) and (x[i] > 0) then begin
          arrX[p] := x[i];
          arrY[p] := y[i];
          p += 1;
        end;
      Result := new CoordContainer.Container(arrX, arrY);
      end;
    end;
begin
  
end.