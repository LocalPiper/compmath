package utils;

public enum InteractorOutputs {
    GREETING("""
            CompLab1 by LocalPiper
                """),
    OPTIONS("""
            Select from the following:
            f - input matrix from file
            m - input matrix manually
                """),
    BY_FILE("""
            File should have this structure:
            n
            a11 a12 ... a1n
            a21 a22 ... a2n
            ... ... ... ...
            an1 an2 ... ann
            where n - dimension of matrix
            For examle, file contents may look like this:
            3
            1 2 3
            4 5 6
            7 8 9
            Make sure your file has this structure, otherwise parsing will fail
            Print file name:
                """),
    BY_HAND("""
            Follow instructions below:
            """),
    ERR_OPTION_NOT_FOUND("""
            Error: option not found. Try again
                """),
    ERR_FILE_NOT_FOUND("""
            Error: requested file not found
                """),
    ERR_INVALID_STRUCTURE("""
            Error: contents don't satisfy structure requirements
                """),
    ERR_UNKNOWN("""
            Error: unknown
            """);

    public final String label;

    private InteractorOutputs(String label) {
        this.label = label;
    }
}
