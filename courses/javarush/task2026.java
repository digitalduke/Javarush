/*
Алгоритмы-прямоугольники

1. Дан двумерный массив N*N, который содержит несколько прямоугольников.
2. Различные прямоугольники не соприкасаются и не накладываются.
3. Внутри прямоугольник весь заполнен 1.
4. В массиве:
4.1) a[i, j] = 1, если элемент (i, j) принадлежит какому-либо прямоугольнику
4.2) a[i, j] = 0, в противном случае
5. getRectangleCount должен возвращать количество прямоугольников.

*/

package com.javarush.task.task20.task2026;

import java.util.HashMap;
import java.util.Map;

/*
Алгоритмы-прямоугольники
*/
public class Solution {
    public static void main(String[] args) {
        byte[][] a1 = new byte[][]{
                {0, 0, 0, 0},
                {0, 1, 1, 0},
                {0, 1, 1, 0},
                {0, 0, 0, 0}
        };
        byte[][] a2 = new byte[][]{
                {1, 0, 0, 1},
                {0, 0, 0, 0},
                {0, 0, 0, 0},
                {1, 0, 0, 1}
        };

        int count1 = getRectangleCount(a1);
        System.out.println("count = " + count1 + ". Должно быть 1");
        int count2 = getRectangleCount(a2);
        System.out.println("count = " + count2 + ". Должно быть 4");
    }

    public static int getRectangleCount(byte[][] a) {
        int rectCount = 0;

        for (int x = 0; x < a.length; x++) {
            for (int y = 0; y < a.length; y++) {
                if (a[x][y] == 1) {
                    int height = findHeight(a, x, y);
                    int width = findWidth(a, y, x);
                    rectCount++;
                    // erasing rectangle
                    for (int i = x; i < height + 1; i++) {
                        for (int j = y; j < width + 1; j++) {
                            a[i][j] = 0;
                        }
                    }

                }
            }
        }

        return rectCount;
    }

    public static int findHeight(byte[][] arr, int startX, int lineY) {
        int endPosition = startX;

        while (endPosition < arr.length - 1) {
            if (arr[endPosition + 1][lineY] == 0)
                return endPosition;
            endPosition++;
        }

        return endPosition;
    }

    public static int findWidth(byte[][] arr, int startY, int lineX) {
        int endPosition = startY;

        while (endPosition < arr.length - 1) {
            if (arr[lineX][endPosition + 1] == 0)
                return endPosition;
            endPosition++;
        }

        return endPosition;
    }

}
