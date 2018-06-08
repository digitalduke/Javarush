package com.javarush.task.task20.task2027;

import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.List;

/*
Кроссворд

1. Дан двумерный массив, который содержит буквы английского алфавита в нижнем регистре.
2. Метод detectAllWords должен найти все слова из words в массиве crossword.
3. Элемент(startX, startY) должен соответствовать первой букве слова, элемент(endX, endY) - последней.
text - это само слово, располагается между начальным и конечным элементами
4. Все слова есть в массиве.
5. Слова могут быть расположены горизонтально, вертикально и по диагонали как в нормальном, так и в обратном порядке.

*/

public class Solution {
    public static void main(String[] args) {
        int[][] crossword = new int[][]{
                {'f', 'd', 'e', 'r', 'l', 'h'},
                {'u', 's', 'a', 'm', 'e', 'o'},
                {'l', 'n', 'g', 'r', 'o', 'v'},
                {'m', 'l', 'p', 'r', 'r', 'h'},
                {'a', 'm', 'a', 'h', 'o', 'm'}
        };

        List<Word> words = detectAllWords(crossword, "home", "same");

        for (Word word: words) {
            System.out.println(word);
        }
    }

    public static List<Word> detectAllWords(int[][] crossword, String... words) {
        List<Word> result = new ArrayList<>();
        AbstractMap.SimpleEntry<Integer, Integer> endPoint;
        int[][] direction = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {1, -1}, {-1, -1}, {-1, 1}};

        // проход по каждому символу матрицы
        for (int y = 0; y < crossword.length; y++) {
            for (int x = 0; x < crossword[0].length; x++) {

                // для каждого искомого слова
                for (String word: words) {
                    // если первая буква совпадает - продолжаем поиск по векторам
                    if (crossword[y][x] == word.charAt(0)) {
                        if (word.length() > 1) {
                            // поиск по векторам
                            for (int vector = 0; vector < 8; vector++) {
                                endPoint = findEnd(crossword, word, x, y, direction[vector][0], direction[vector][1]);
                                if (endPoint != null) {
                                    Word foundedWord = new Word(word);
                                    foundedWord.setStartPoint(x, y);
                                    foundedWord.setEndPoint(endPoint.getKey(), endPoint.getValue());
                                    result.add(foundedWord);
                                }
                            }
                        } else {
                            // слово однобуквенное - странно, ну и ладно
                            // данное условие не обязательно для валидатора javarush
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
        boolean wordFounded = true;

        try {
            for (int l = 1; l < word.length(); l++) {
                // прибавляем вектор
                endX += incX;
                endY += incY;
                // если следующая буква не совпадает, значит не то слово
                if (crossword[endY][endX] != word.charAt(l)) {
                    wordFounded = false;
                    break; // нет смысла продолжать
                }
            }
        } catch (Exception ignored) {
            // вышли за границы матрицы - значит точно ничего не нашли
            wordFounded = false;
        }

        if (wordFounded) {
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
