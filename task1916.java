package com.javarush.task.task19.task1916;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/*
Отслеживаем изменения

Считать с консоли 2 имени файла - file1, file2.
Файлы содержат строки, file2 является обновленной версией file1, часть строк совпадают.
Нужно создать объединенную версию строк, записать их в список lines.
Операции ADDED и REMOVED не могут идти подряд, они всегда разделены SAME.
В оригинальном и редактируемом файлах пустых строк нет!

Пример:
оригинальный    редактированный    общий
file1:          file2:             результат:(lines)
 
строка1         строка1            SAME строка1
строка2                            REMOVED строка2
строка3         строка3            SAME строка3
строка4                            REMOVED строка4
строка5         строка5            SAME строка5
                строка0            ADDED строка0
строка1         строка1            SAME строка1
строка2                            REMOVED строка2
строка3         строка3            SAME строка3
                строка4            ADDED строка4
строка5         строка5            SAME строка5
строка0                            REMOVED строка0

Пустые строки в примере означают, что этой строки нет в определенном файле.


*/

public class Solution {
    public static List<LineItem> lines = new ArrayList<LineItem>();

    public static void main(String[] args) throws IOException {
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        List<String> linesOne = new ArrayList<>();
        List<String> linesTwo = new ArrayList<>();

        String fNameOne = console.readLine();
        String fNameTwo = console.readLine();
        //String fNameOne = "c:\\lines1.txt", fNameTwo = "c:\\lines2.txt";
        console.close();

        FileReader fReader = new FileReader(fNameOne);
        BufferedReader reader = new BufferedReader(fReader);
        while (reader.ready()) {
            linesOne.add(reader.readLine());
        }
        fReader.close();

        fReader = new FileReader(fNameTwo);
        reader = new BufferedReader(fReader);
        while (reader.ready()) {
            linesTwo.add(reader.readLine());
        }
        fReader.close();

        int p1 = 0;
        int p2 = 0;
        int p1Max = linesOne.size() - 1;
        int p2Max = linesTwo.size() - 1;
        int i1 = 0;
        int i2 = 0;
        boolean firstCanExit = false;
        boolean secondCanExit = false;

        while (!(firstCanExit && secondCanExit)) {

            if (p1 == p1Max) firstCanExit = true;
            if (p2 == p2Max) secondCanExit = true;

            i1 = Integer.parseInt(linesOne.get(p1).replace("строка", ""));
            i2 = Integer.parseInt(linesTwo.get(p2).replace("строка", ""));

            if (i1 == i2) {
                System.out.println("SAME " + linesOne.get(p1));
                lines.add(new LineItem(Type.SAME, linesOne.get(p1)));
                p1++;
                p2++;

            } else {

                if (i1 < i2) {
                    System.out.println("REMOVED " + linesOne.get(p1));
                    lines.add(new LineItem(Type.REMOVED, linesOne.get(p1)));
                    p1++;
                } else {

                    if (i1 > i2) {
                        System.out.println("ADDED " + linesTwo.get(p2));
                        lines.add(new LineItem(Type.ADDED, linesOne.get(p2)));
                        p2++;
                    }

                }
            }

        }

    }


    public static enum Type {
        ADDED,        //добавлена новая строка
        REMOVED,      //удалена строка
        SAME          //без изменений
    }

    public static class LineItem {
        public Type type;
        public String line;

        public LineItem(Type type, String line) {
            this.type = type;
            this.line = line;
        }
    }
}
