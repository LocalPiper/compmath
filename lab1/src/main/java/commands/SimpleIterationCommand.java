package main.java.commands;

import main.java.receivers.IterationalMethodCommandReceiver;
import main.java.structures.MatrixPacket;
import main.java.structures.ResultPacket;

public class SimpleIterationCommand implements Command {
    public ResultPacket execute(MatrixPacket mp) {
        return new IterationalMethodCommandReceiver().simpleIterationMethod(mp);
    }

}
