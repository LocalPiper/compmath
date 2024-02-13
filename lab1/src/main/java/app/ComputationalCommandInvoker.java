package app;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import commands.Command;
import commands.GaussCommand;
import commands.GaussSeidelCommand;
import commands.ModifiedGaussCommand;
import commands.SimpleIterationCommand;
import structures.MatrixPacket;
import structures.ResultPacket;
import utils.InvokerOutputs;

public class ComputationalCommandInvoker {
    private void print(InvokerOutputs io) {
        System.out.println(io.label);
    }

    private String getUserCommand() throws IOException {
        List<String> commands = new ArrayList<>();
        commands.add("g");
        commands.add("mg");
        commands.add("si");
        commands.add("gs");
        print(InvokerOutputs.OPTIONS);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String command = br.readLine().trim();
        if (!commands.contains(command.trim())) {
            command = commands.get(0);
        }
        return command;
    }

    public ResultPacket invoke(MatrixPacket mp) throws IOException {
        Map<String, Command> commandHashMap = new HashMap<>();
        commandHashMap.put("g", new GaussCommand());
        commandHashMap.put("mg", new ModifiedGaussCommand());
        commandHashMap.put("si", new SimpleIterationCommand());
        commandHashMap.put("gs", new GaussSeidelCommand());

        commandHashMap.get(getUserCommand()).execute(mp);
        return new ResultPacket();
    }
}
