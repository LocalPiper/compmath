package main.java.utils;

public enum InvokerOutputs {
    OPTIONS("""
            Select from the following:
            g  - Gauss method
            mg - Modified Gauss method
            si - Simple Iteration method
            gs - Gauss-Seidel method
            Gauss method is selected by default
            """),
    STANDBY("""
            Loading...
            """),
    ERR_INVALID_METHOD("""
            Error: couldn't recognize method. Default method will be used
            """);

    public final String label;

    InvokerOutputs(String label) {
        this.label = label;
    }
}
