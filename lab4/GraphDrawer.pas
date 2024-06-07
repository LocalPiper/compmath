unit GraphDrawer;

interface

uses Container, Approximations, GraphWPF, Utils;

procedure DrawEverything(x, y: array of real; c1: Container.Container2; c2: Container.Container3; c3: Container.Container4; c4, c5, c6: Container.Container2);
implementation

function GenerateArray(Size: integer; Start, Spacing: real): array of real;
begin
  var arr := new real[Size];
  for var i := 0 to Size - 1 do
  begin
    arr[i] := Start;
    Start += Spacing;
  end;
  Result := arr;
end;

procedure DrawEverything(x, y: array of real; c1: Container.Container2; c2: Container.Container3; c3: Container.Container4; c4, c5, c6: Container.Container2);
begin
  {start setting coord pane}
  var Scaling: real := 1;
  SetStandardCoords(Scaling, Window.Center.X, Window.Center.Y);
  Arrow(-Window.Center.X, 0, Window.Center.X, 0);
  Arrow(0, Window.Center.Y, 0, -Window.Center.Y);
  
  {prepare plotting array}
  var NumberOfPoints: integer := 1000;
  var Spacing: real := Window.Width / NumberOfPoints;
  var GraphingArrayX := GenerateArray(NumberOfPoints, -Window.Center.X, Spacing);
  
  
  
  {become one with PascalABCNet and it's cOmPrEhEnSiVe dOcUmEnTaTiOn}
  Pen.Color := RGB(0, 0, 255);
  var GraphingArrayY := ApplyApproximation2(GraphingArrayX, c1.sa, c1.sb, LinearApproximation);
  for var i := 0 to GraphingArrayY.Length - 2 do
    Line(GraphingArrayX[i], -GraphingArrayY[i], GraphingArrayX[i + 1], -GraphingArrayY[i + 1]);
  
  Pen.Color := RGB(0, 255, 0);
  GraphingArrayY := ApplyApproximation3(GraphingArrayX, c2.sa, c2.sb, c2.sc, PolynomialApproximation2);
  for var i := 0 to GraphingArrayY.Length - 2 do
    Line(GraphingArrayX[i], -GraphingArrayY[i], GraphingArrayX[i + 1], -GraphingArrayY[i + 1]);
  
  Pen.Color := RGB(255, 255, 0);
  GraphingArrayY := ApplyApproximation4(GraphingArrayX, c3.sa, c3.sb, c3.sc, c3.sd, PolynomialApproximation3);
  for var i := 0 to GraphingArrayY.Length - 2 do
    Line(GraphingArrayX[i], -GraphingArrayY[i], GraphingArrayX[i + 1], -GraphingArrayY[i + 1]);
  
  Pen.Color := RGB(0, 255, 255);
  GraphingArrayY := ApplyApproximation2(GraphingArrayX, c4.sa, c4.sb, PowerApproximation);
  for var i := 0 to GraphingArrayY.Length - 2 do
    Line(GraphingArrayX[i], -GraphingArrayY[i], GraphingArrayX[i + 1], -GraphingArrayY[i + 1]);
  
  Pen.Color := RGB(255, 0, 255);
  GraphingArrayY := ApplyApproximation2(GraphingArrayX, c5.sa, c5.sb, ExponentialApproximation);
  for var i := 0 to GraphingArrayY.Length - 2 do
    Line(GraphingArrayX[i], -GraphingArrayY[i], GraphingArrayX[i + 1], -GraphingArrayY[i + 1]);
  
  Pen.Color := RGB(102, 0, 102);
  GraphingArrayY := ApplyApproximation2(GraphingArrayX, c6.sa, c6.sb, LogarithmicApproximation);
  for var i := 0 to GraphingArrayY.Length - 2 do
    Line(GraphingArrayX[i], -GraphingArrayY[i], GraphingArrayX[i + 1], -GraphingArrayY[i + 1]);
  
  {draw existing points}
  Brush.Color := RGB(255, 0, 0);
  for var i := 0 to x.Length - 1 do
  begin
    FillCircle(x[i], -y[i], 2);
  end;
  {this text is static, no idea how to make it scale with the window}
  DrawText(Window.Center.X - 100, -Window.Center.Y + 10, 10, 10, 'Blue - linear');
  DrawText(Window.Center.X - 100, -Window.Center.Y + 30, 10, 10, 'Green - polynomial2');
  DrawText(Window.Center.X - 100, -Window.Center.Y + 50, 10, 10, 'Yellow - polynomial3');
  DrawText(Window.Center.X - 100, -Window.Center.Y + 70, 10, 10, 'Cyan - power');
  DrawText(Window.Center.X - 100, -Window.Center.Y + 90, 10, 10, 'Pink - exponential');
  DrawText(Window.Center.X - 100, -Window.Center.Y + 110, 10, 10, 'Purple - logarithmic');
end;

begin
end. 
