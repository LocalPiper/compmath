package main.java.utils;

public enum MatrixReaderOutputs {
    REQUEST_DIMENSION {
        @Override
        public void request(String arg) {
            print("Input dimension:");
        }
    },
    REQUEST_LINE {
        @Override
        public void request(String arg) {
            print("Input line (coefficients) like this: a" + arg + "1 a" + arg + "2 a" + arg + "3 and so on");
        }
    };

    public abstract void request(String arg);

    private static void print(String message) {
        System.out.println(message);
    }
}
