unit Container;
interface
type
  Container2 = class
  public
    sR2 : real;
    sa : real;
    sb : real;
    constructor Create(R2 : real; a : real; b : real);
      begin
         sR2 := R2;
         sa := a;
         sb := b;
      end;
  end;
type
  Container3 = class
  public
    sR2 : real;
    sa : real;
    sb : real;
    sc : real;
    constructor Create(R2 : real; a : real; b : real; c : real);
      begin
         sR2 := R2;
         sa := a;
         sb := b;
         sc := c;
      end;
  end;
type
  Container4 = class
  public
    sR2 : real;
    sa : real;
    sb : real;
    sc : real;
    sd : real;
    constructor Create(R2 : real; a : real; b : real; c : real; d : real);
      begin
         sR2 := R2;
         sa := a;
         sb := b;
         sc := c;
         sd := d;
      end;
  end;
implementation
begin
end.