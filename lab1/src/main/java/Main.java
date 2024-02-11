package main.java;

import java.io.IOException;

import main.java.io.UserInteractor;

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
