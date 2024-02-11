package main.java.io;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import main.java.utils.InteractorOutputs;

public class UserInteractor {

    private void print(InteractorOutputs message) {
        System.out.println(message.label);
    }

    public void interact() throws IOException {
        print(InteractorOutputs.GREETING);
        print(InteractorOutputs.OPTIONS);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean done = false;
        char option;
        while (!done) {
            option = br.readLine().charAt(0);
            switch (option) {
                case 'f':
                    handleFile();
                    done = true;
                    break;
                case 'm':
                    handleManual();
                    done = true;
                    break;
                default:
                    print(InteractorOutputs.ERR_OPTION_NOT_FOUND);
                    break;
            }
        }
    }

    private void handleFile() throws IOException {
        print(InteractorOutputs.BY_FILE);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String filename = br.readLine();
        MatrixReader matrixReader = new MatrixReader();
    }

    private void handleManual() throws IOException {
        print(InteractorOutputs.BY_HAND);
        MatrixReader matrixReader = new MatrixReader();
    }
}
