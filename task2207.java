package com.javarush.task.task22.task2207;

import java.io.*;
import java.util.*;

/*
Обращенные слова

В методе main с консоли считать имя файла, который содержит слова, разделенные пробелами.
Найти в тексте все пары слов, которые являются обращением друг друга. Добавить их в result.
Использовать StringBuilder.
Кодировка файла - UTF-8.

Пример содержимого файла
рот тор торт о
о тот тот тот

Вывод:
рот тор
о о
тот тот

*/
public class Solution {
    public static List<Pair> result = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        String[] words;
        StringBuilder buffer = new StringBuilder();
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        String filename = console.readLine();

        BufferedReader file = new BufferedReader(new FileReader(filename));
        while (file.ready()) {
            buffer.append(file.readLine());
            buffer.append(' ');
        }

        words = buffer.toString().split(" ");

        for (int i = 0; i < words.length; i++) {
            for (int n = i + 1; n < words.length; n++) {
                StringBuilder testWord = new StringBuilder(words[i]);
                StringBuilder reverse = new StringBuilder(words[n]);

                if (testWord.toString().equals(reverse.reverse().toString())) {
                    addUnique(testWord.toString(), reverse.reverse().toString());
                    break;
                }
            }
        }

        for (Pair entry: result) {
            System.out.println(entry);
        }

    }

    public static void addUnique(String word, String reverseWord) {
        Boolean unique = true;

        for (Pair pair: result) {
            if (pair.first.equals(word)) {
                unique = false;
                break;
            }
        }

        if (unique) {
            result.add(new Pair(word, reverseWord));
        }
    }

    public static class Pair {
        String first;
        String second;

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            Pair pair = (Pair) o;

            if (first != null ? !first.equals(pair.first) : pair.first != null) return false;
            return second != null ? second.equals(pair.second) : pair.second == null;

        }

        @Override
        public int hashCode() {
            int result = first != null ? first.hashCode() : 0;
            result = 31 * result + (second != null ? second.hashCode() : 0);
            return result;
        }

        @Override
        public String toString() {
            return  first == null && second == null ? "" :
                    first == null && second != null ? second :
                            second == null && first != null ? first :
                                    first.compareTo(second) < 0 ? first + " " + second : second + " " + first;

        }

        public Pair() {
        }

        public Pair(String first, String second) {
            this.first = first;
            this.second = second;
        }
    }

}
