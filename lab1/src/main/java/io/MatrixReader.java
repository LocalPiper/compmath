package io;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import structures.MatrixPacket;
import utils.MatrixReaderOutputs;

public class MatrixReader {
    public MatrixPacket readFromFile(String filename) {
        try (Scanner scanner = new Scanner(Paths.get(filename))) {
            int dimension = scanner.nextInt();
            List<Double> rawMatrix = new ArrayList<>();
            while (scanner.hasNext()) {
                if (scanner.hasNextDouble()) {
                    rawMatrix.add(scanner.nextDouble());
                } else {
                    scanner.next();
                }
            }
            if (rawMatrix.size() != dimension * dimension) {
                throw new ArrayIndexOutOfBoundsException();
            }
            MatrixPacket mp = new MatrixPacket();
            mp.fillWithRaw(dimension, rawMatrix);
            return mp;
        } catch (ArrayIndexOutOfBoundsException e) {
            MatrixPacket mp = new MatrixPacket();
            mp.fillWithRaw(-2, new ArrayList<>());
            return mp;
        } catch (IOException e) {
            MatrixPacket mp = new MatrixPacket();
            mp.fillWithRaw(-1, new ArrayList<>());
            return mp;
        }

    }

    public MatrixPacket readFromConsole() {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        MatrixReaderOutputs.REQUEST_DIMENSION.request("");
        try {
            int dimension = Integer.parseInt(br.readLine());
            List<List<Double>> matrix = new ArrayList<>();
            for (int i = 0; i < dimension; ++i) {
                MatrixReaderOutputs.REQUEST_LINE.request(String.valueOf(i + 1));
                List<Double> list = new ArrayList<>();
                String[] nums = br.readLine().split(" ");
                if (nums.length != dimension) {
                    throw new ArrayIndexOutOfBoundsException();
                }
                for (int j = 0; j < dimension; ++j) {
                    list.add(Double.parseDouble(nums[j]));
                }
                matrix.add(list);
            }
            MatrixPacket mp = new MatrixPacket();
            mp.fill(dimension, matrix);
            return mp;
        } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) {
            MatrixPacket mp = new MatrixPacket();
            mp.fillWithRaw(-2, new ArrayList<>());
            return mp;
        } catch (IOException e) {
            MatrixPacket mp = new MatrixPacket();
            mp.fillWithRaw(-1, new ArrayList<>());
            return mp;
        }

    }
}
