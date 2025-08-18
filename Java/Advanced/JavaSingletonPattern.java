import java.util.Scanner;
import java.lang.reflect.Constructor;

class Singleton {

    public String str;

    // single private static instance
    private static Singleton instance = null;

    // private constructor
    private Singleton() {}

    // static method to get single instance
    public static Singleton getSingleInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
