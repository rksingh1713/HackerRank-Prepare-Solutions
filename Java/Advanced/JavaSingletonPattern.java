class Singleton {

  public String str;

  private Singleton() {}

  public static Singleton getSingleInstance() {
    return new Singleton();
  }
}

public class JavaSingletonPattern {

  public static void main(String[] args) {}
}
