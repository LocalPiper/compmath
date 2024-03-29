package structures;

import java.util.ArrayList;
import java.util.List;

public class MatrixPacket {
    private int dimension;
    private List<List<Double>> matrix;

    public void fillWithRaw(int dimension, List<Double> rawMatrix) {
        this.dimension = dimension;
        this.matrix = new ArrayList<>();
        int i = 0;
        while (i < this.dimension) {
            int j = 0;
            List<Double> list = new ArrayList<>();
            while (j < this.dimension) {
                list.add(rawMatrix.get(i * dimension + j));
                ++j;
            }
            this.matrix.add(list);
            ++i;
        }
    }

    public void fill(int dimension, List<List<Double>> matrix) {
        this.dimension = dimension;
        this.matrix = matrix;
    }

    public int getDimension() {
        return dimension;
    }

    public List<List<Double>> getMatrix() {
        return matrix;
    }

    public void setMatrix(List<List<Double>> newMatrix) {
        this.matrix.clear();
        this.matrix.addAll(newMatrix);
    }

    public void outputMatrix() {
        System.out.println("Matrix of dimension " + dimension);
        for (List<Double> list : matrix) {
            for (double val : list) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public List<Double> getDiagonal() {
        List<Double> diagonal = new ArrayList<>();
        for (int i = 0; i < dimension; ++i) {
            diagonal.add(matrix.get(i).get(i));
        }
        return diagonal;
    }
}
