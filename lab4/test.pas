uses LinearSolver, Polynomial2Solver, Polynomial3Solver, PowerSolver, ExponentialSolver, LogarithmicSolver, Utils, Container, GraphDrawer, CoordContainer, ArraySanitizer;
label FINISH;
begin
  
  {here lies LocalPiper. He was determined to do this lab using this language (because he was told to do so)}
  {he died trying to battle poor .NET compatibility, brief documentation and lack of information about the issues of this garbage PL}
  {R.I.P. you will not be missed}
  writeln('CompLab#4 by LocalPiper');
  writeln;
  
  writeln('Input file name: ');
  
  var filename: string;
  
  read(filename);
  var cc := new CoordContainer.FileCoordContainer(filename);
  var x := cc.x;
  var y := cc.y;
  
  writeln('Arrays of (x, y): ');
  PrintVector(x, y);
  
  if not CheckHealth(x, y) then begin
    writeln('Terminating...');
    goto FINISH;
  end;
  writeln;
  var c1: Container2 := LinearSolver.Solve(x, y);
  writeln;
  var c2: Container3 := Polynomial2Solver.Solve(x, y);
  writeln;
  var c3: Container4 := Polynomial3Solver.Solve(x, y);
  writeln;
  var c4: Container2 := PowerSolver.Solve(x, y);
  writeln;
  var c5: Container2 := ExponentialSolver.Solve(x, y);
  writeln;
  var c6: Container2 := LogarithmicSolver.Solve(x, y);
  writeln;
  DrawEverything(x, y, c1, c2, c3, c4, c5, c6);
  
  writeln;
  writeln('Determination: ');
  writeln('Linear: ' + c1.sR2);
  writeln('Polynomial2: ' + c2.sR2);
  writeln('Polynomial3: ' + c3.sR2);
  writeln('Power: ' + c4.sR2);
  writeln('Exponential: ' + c5.sR2);
  writeln('Logarithmic: ' + c6.sR2);
FINISH:
end.