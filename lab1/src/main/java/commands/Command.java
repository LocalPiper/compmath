package main.java.commands;

import main.java.structures.MatrixPacket;
import main.java.structures.ResultPacket;

@FunctionalInterface
public interface Command {
    ResultPacket execute(MatrixPacket mp);
}
