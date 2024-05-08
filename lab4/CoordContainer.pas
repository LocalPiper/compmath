unit CoordContainer;

interface

type
  FileCoordContainer = class
  public
    x: array of real;
    y: array of real;
    constructor Create(FileName: string);
    begin
      var f: text;
      assign(f, FileName);
      try
        reset(f);
        var n: integer := 0;
        read(f, n);
        x := new real[n];
        y := new real[n];
        for var i := 0 to n - 1 do
          read(f, x[i]);
        for var i := 0 to n - 1 do
          read(f, y[i]);
        close(f);
      except
        on System.IO.FileNotFoundException do begin
          writeln('ERROR: File not found!');
          x := new real[0];
          y := new real[0];
          exit;
        end;
        on System.FormatException do begin
          writeln('ERROR:File corrupted!');
          x := new real[0];
          y := new real[0];
          exit;
        end;
      end;
    end;
  end;

type
  Container = class
  public
    x: array of real;
    y: array of real;
    constructor Create(xx, yy: array of real);
    begin
      x := xx;
      y := yy;
    end;
  end;

implementation

begin

end. 