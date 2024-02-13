package commands;

import structures.MatrixPacket;
import structures.ResultPacket;

@FunctionalInterface
public interface Command {
    ResultPacket execute(MatrixPacket mp);
}
