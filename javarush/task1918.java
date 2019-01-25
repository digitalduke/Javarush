package com.javarush.task.task19.task1918;

/* 
Знакомство с тегами

Считайте с консоли имя файла, который имеет HTML-формат.

Пример:
Info about Leela <span xml:lang="en" lang="en"><b><span>Turanga Leela
</span></b></span><span>Super</span><span>girl</span>

Первым параметром в метод main приходит тег. Например, "span".
Вывести на консоль все теги, которые соответствуют заданному тегу.
Каждый тег на новой строке, порядок должен соответствовать порядку следования в файле.
Количество пробелов, \n, \r не влияют на результат.
Файл не содержит тег CDATA, для всех открывающих тегов имеется отдельный закрывающий тег, одиночных тегов нет.
Тег может содержать вложенные теги.

Пример вывода:
<span xml:lang="en" lang="en"><b><span>Turanga Leela</span></b></span>
<span>Turanga Leela</span>
<span>Super</span>
<span>girl</span>

Шаблон тега:
<tag>text1</tag>
<tag text2>text1</tag>
<tag
text2>text1</tag>

text1, text2 могут быть пустыми
*/

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader console = new BufferedReader(new InputStreamReader(System.in));
        String fName = console.readLine();
        //String fName = "c:\\1.txt";
        console.close();

        FileReader reader = new FileReader(fName);
        StringBuffer htmlText = new StringBuffer();

        while (reader.ready()) {
            int b = reader.read();
            if ((char)b != '\n' && (char)b != '\r') {
                htmlText.append((char)b);
            }
        }

        String tag = args[0];
        Pattern pattern = Pattern.compile("<" + tag, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(htmlText);

        while (matcher.find()) {
            String tmpStr = htmlText.substring(matcher.start(), tagEnd(tag, htmlText, matcher.end()));
            System.out.println(tmpStr);
        }

        reader.close();
    }

    static int tagEnd(String tag, StringBuffer where, int startPosition) {
        Pattern tagStartPattern = Pattern.compile("<" + tag, Pattern.CASE_INSENSITIVE);
        Pattern tagEndPattern = Pattern.compile("<\\/" + tag + ">", Pattern.CASE_INSENSITIVE);

        Matcher tagStartMatcher = tagStartPattern.matcher(where);
        Matcher tagEndMatcher = tagEndPattern.matcher(where);

        if (!tagStartMatcher.find(startPosition)) {
            // не нашли <tag> - возвращаем окончание </tag>
            tagEndMatcher.find(startPosition);
            return tagEndMatcher.end();
        } else {
            // нашли <tag> ищем </tag>
            tagEndMatcher.find(startPosition);
            if (tagStartMatcher.start() < tagEndMatcher.start()) {
                // <tag> раньше чем </tag> - рекурсим
                return tagEnd(tag, where, tagEndMatcher.end());
            } else {
                // </tag> раньше чем <tag> - возвращаем окончание
                return tagEndMatcher.end();
            }
        }

    }
}
