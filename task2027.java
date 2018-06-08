package com.javarush.task.task20.task2027;

import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.List;

/*
Кроссворд
*/
public class Solution {
    public static void main(String[] args) {
        int[][] crossword = new int[][]{
                {'f', 'd', 'e', 'r', 'l', 'k'},
                {'u', 's', 'a', 'm', 'e', 'o'},
                {'l', 'n', 'g', 'r', 'o', 'v'},
                {'m', 'l', 'p', 'r', 'r', 'h'},
                {'e', 'm', 'a', 's', 'j', 'j'}
        };
        //detectAllWords(crossword, "home", "same");
        List<Word> words = detectAllWords(crossword, "fde", "same", "j", "home");
        for (Word word: words) {
            System.out.println(word);
        }
        /*
Ожидаемый результат
home - (5, 3) - (2, 0)
same - (1, 1) - (4, 1)
         */
    }

    public static List<Word> detectAllWords(int[][] crossword, String... words) {
        List<Word> result = new ArrayList<>();
        AbstractMap.SimpleEntry<Integer, Integer> endPoint;
        int[] vectorX = {1, -1, 0, 0, 1, 1, -1, -1};
        int[] vectorY = {0, 0, 1, -1, 1, -1, -1, 1};

        // проход по каждому символу матрицы
        for (int y = 0; y < crossword.length; y++) {
            for (int x = 0; x < crossword[0].length; x++) {

                // для каждого искомого слова
                for (String word: words) {
                    // первая буква совпадает - начинаем поиск по векторам
                    if (crossword[y][x] == word.charAt(0)) {
                        if (word.length() > 1) {
                            // поиск по векторам
                            for (int vector = 0; vector < 8; vector++) {
                                endPoint = findEnd(crossword, word, x, y, vectorX[vector], vectorY[vector]);
                                if (endPoint != null) {
                                    Word foundedWord = new Word(word);
                                    foundedWord.setStartPoint(x, y);
                                    foundedWord.setEndPoint(endPoint.getKey(), endPoint.getValue());
                                    result.add(foundedWord);
                                }
                            }
                        } else {
                            // слово однобуквенное - странно, ну и ладно
                            Word foundedWord = new Word(word);
                            foundedWord.setStartPoint(x, y);
                            foundedWord.setEndPoint(x, y);
                            result.add(foundedWord);
                        }
                    }

                }
            }
        }


        return result;
    }

    private static AbstractMap.SimpleEntry<Integer, Integer> findEnd(int[][] crossword, String word, int startX, int startY, int incX, int incY) {
        int endX = startX, endY = startY;
        boolean wordFounded = false;

        try {
            for (int l = 1; l < word.length(); l++) {
                endX += incX;
                endY += incY;
                wordFounded = crossword[endY][endX] == word.charAt(l);
            }
        } catch (Exception ignored) {
            // вышли за границы матрицы - ну и хрен с ним
        }

        if (wordFounded) {
            //System.out.println("найдено вхождение: " + word + " startX " + startX
            //        + " startY " + startY
            //        + " endX " + endX
            //        + " endY " + endY);
            AbstractMap.SimpleEntry<Integer, Integer> endPoint = new AbstractMap.SimpleEntry<>(endX, endY);
            return endPoint;
        }

    return null;

    }

    public static class Word {
        private String text;
        private int startX;
        private int startY;
        private int endX;
        private int endY;

        public Word(String text) {
            this.text = text;
        }

        public void setStartPoint(int i, int j) {
            startX = i;
            startY = j;
        }

        public void setEndPoint(int i, int j) {
            endX = i;
            endY = j;
        }

        @Override
        public String toString() {
            return String.format("%s - (%d, %d) - (%d, %d)", text, startX, startY, endX, endY);
        }
    }
}
