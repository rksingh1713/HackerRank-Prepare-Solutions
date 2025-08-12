import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

public class JavaPriorityQueue {

  private static final Scanner scan = new Scanner(System.in);
  private static final Priorities priorities = new Priorities();

  public static class Students implements Comparable<Students> {

    private int id;
    private String name;
    private Double cgpa;

    public Students(int id, String name, Double cgpa) {
      this.id = id;
      this.name = name;
      this.cgpa = cgpa;
    }

    public int getId() {
      return id;
    }

    public String getName() {
      return name;
    }

    public Double getCgpa() {
      return cgpa;
    }

    @Override
    public int compareTo(Students a) {
      if ((Double.compare(a.getCgpa(), this.cgpa) == 0) && (a.name.compareTo(this.name) == 0)) {
        return Integer.compare(a.id, this.id);
      } else if ((Double.compare(a.getCgpa(), this.cgpa) == 0)) {
        return this.name.compareTo(a.name);
      } else{
        return Double.compare(a.getCgpa(), this.cgpa);
      }
    }
  }

  public static class Priorities {

    public List<Students> getStudents(List<String> events) {
      PriorityQueue<Students> queue = new PriorityQueue<>();

      for (String event : events) {
        Scanner scanner = new Scanner(event);
        String command = scanner.next();

        switch (command) {
          case "ENTER":
            String name = scanner.next();
            Double cgpa = scanner.nextDouble();
            int id = scanner.nextInt();
            Students student = new Students(id, name, cgpa);
            queue.add(student);

            break;
          case "SERVED":
            if (!queue.isEmpty()) {
              queue.poll();
            }

            break;
        }
        scanner.close();
      }

      List<Students> studentList = new ArrayList<>();
      while (!queue.isEmpty()) {
        studentList.add(queue.poll());
      }
      return studentList;
    }
  }

  public static void main(String[] args) {
    Long totalEvents = Long.parseLong(scan.nextLine());
    List<String> events = new ArrayList<>();

    while (totalEvents-- != 0) {
      String event = scan.nextLine();
      events.add(event);
    }

    List<Students> students = priorities.getStudents(events);

    if (students.isEmpty()) {
      System.out.println("EMPTY");
    } else {
      for (Students st : students) {
        System.out.println(st.getName());
      }
    }
  }
}
