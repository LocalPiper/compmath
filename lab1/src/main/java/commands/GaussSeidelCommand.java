package commands;

import receivers.IterationalMethodCommandReceiver;
import structures.MatrixPacket;
import structures.ResultPacket;

public class GaussSeidelCommand implements Command {
    public ResultPacket execute(MatrixPacket mp) {
        return new IterationalMethodCommandReceiver().gaussSeidelMethod(mp);
    }
}
