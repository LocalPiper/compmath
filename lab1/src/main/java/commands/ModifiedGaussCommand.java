package commands;

import receivers.LinearMethodCommandReceiver;
import structures.MatrixPacket;
import structures.ResultPacket;

public class ModifiedGaussCommand implements Command {
    public ResultPacket execute(MatrixPacket mp) {
        return new LinearMethodCommandReceiver().modifiedGaussMethod(mp);
    }

}
