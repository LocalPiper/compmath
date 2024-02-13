package app;

import java.io.IOException;

import io.UserInteractor;

public class Main {
    public static void main(String[] args) {
        try {
            UserInteractor userInteractor = new UserInteractor();
            userInteractor.interact();
        } catch (IOException e) {
            System.out.println("Unexpected error occured!");
        }

    }
}
