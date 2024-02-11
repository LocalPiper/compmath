package main.java.commands;

import main.java.receivers.LinearMethodCommandReceiver;
import main.java.structures.MatrixPacket;
import main.java.structures.ResultPacket;

public class ModifiedGaussCommand implements Command {
    public ResultPacket execute(MatrixPacket mp) {
        return new LinearMethodCommandReceiver().modifiedGaussMethod(mp);
    }

}
