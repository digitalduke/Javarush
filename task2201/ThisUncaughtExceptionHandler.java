package com.javarush.task.task22.task2201;

public class ThisUncaughtExceptionHandler implements Thread.UncaughtExceptionHandler {
    @Override
    public void uncaughtException(Thread t, Throwable e) {
        final String string = "%s : %s : %s";
        if (Solution.FIRST_THREAD_NAME.equals(t.getName())) {
            System.out.println(getFormattedStringForFirstThread(t, e, string));
        } else
            if (Solution.SECOND_THREAD_NAME.equals(t.getName())) {
                System.out.println(getFormattedStringForSecondThread(t, e, string));
            } else {
                System.out.println(getFormattedStringForOtherThread(t, e, string));
            }
    }

    protected String getFormattedStringForOtherThread(Thread t, Throwable e, String string) {
        String t1 = t.getName();
        String t2 = e.getClass().getSimpleName();
        String t3 = e.getCause().toString();

        return String.format(string, t2, t3, t1);
    }

    protected String getFormattedStringForSecondThread(Thread t, Throwable e, String string) {
        String t1 = t.getName();
        String t2 = e.getClass().getSimpleName();
        String t3 = e.getCause().toString();

        return String.format(string, t3, t2, t1);
    }

    protected String getFormattedStringForFirstThread(Thread t, Throwable e, String string) {
        String t1 = t.getName();
        String t2 = e.getClass().getSimpleName();
        String t3 = e.getCause().toString();

        return String.format(string, t1, t2, t3);
    }
}

