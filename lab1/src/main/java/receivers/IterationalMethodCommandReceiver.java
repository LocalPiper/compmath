package receivers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

import structures.MatrixPacket;
import structures.ResultPacket;

public class IterationalMethodCommandReceiver {
    private void print(String message) {
        System.out.println(message);
    }

    private boolean checkHealth(List<Double> diag) {
        return !diag.contains(0d);
    }

    private int findIndexOfMax(List<Double> mr) {
        double sum = 0;
        for (double val : mr) {
            sum += Math.abs(val);
        }
        for (int i = 0; i < mr.size(); ++i) {
            if (Math.abs(mr.get(i)) >= (sum - Math.abs(mr.get(i)))) {
                return i;
            }
        }
        return -1;
    }

    public ResultPacket simpleIterationMethod(MatrixPacket mp) {
        // try sorting matrix by diagonal elements
        List<Integer> listOfMax = new ArrayList<>();
        HashSet<Integer> setOfMax = new HashSet<>();
        for (List<Double> l : mp.getMatrix()) {
            setOfMax.add(findIndexOfMax(l));
            listOfMax.add(findIndexOfMax(l));
        }
        if (setOfMax.size() != mp.getDimension() || listOfMax.contains(-1)) {
            print("Couldn't sort matrix by dominating diagonals. Computing until iterations run out...");
        } else {
            List<List<Double>> sortedMatrix = new ArrayList<>();
            for (int i : listOfMax) {
                sortedMatrix.add(mp.getMatrix().get(listOfMax.get(i)));
            }
            mp.setMatrix(sortedMatrix);
            if (!checkHealth(mp.getDiagonal())) {
                // b a d

            } else {

            }
        }
        return new ResultPacket();
    }

    public ResultPacket gaussSeidelMethod(MatrixPacket mp) {
        // TODO: implement
        return new ResultPacket();
    }
}
