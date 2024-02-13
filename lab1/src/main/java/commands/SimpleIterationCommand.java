package commands;

import receivers.IterationalMethodCommandReceiver;
import structures.MatrixPacket;
import structures.ResultPacket;

public class SimpleIterationCommand implements Command {
    public ResultPacket execute(MatrixPacket mp) {
        return new IterationalMethodCommandReceiver().simpleIterationMethod(mp);
    }

}
