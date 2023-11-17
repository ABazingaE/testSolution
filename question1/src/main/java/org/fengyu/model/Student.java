package org.fengyu.model;


import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * @Author: Bazinga
 * @Date: 2023/11/17 - 11 - 17 - 23:38
 * @Description:
 * 问题 4 请设计结构体类型（或类类型）自定义数据，完成对上述单个学生
 * 信息的记录，其中对于性别和专业请使用枚举类型进行限定。并将所有同学的信
 * 息存放在你所构建的数据类型数组中。
 * @Version: 1.0
 */
public class Student {
    public enum Gender { MALE, FEMALE }
    public enum Major { IoT, AI, CS, DM }

    private String name;
    private Gender gender;
    private Major major;
    private int score;

    public Student(String name, Gender gender, Major major, int score) {
        this.name = name;
        this.gender = gender;
        this.major = major;
        this.score = score;
    }

    /*
    * 初始化题干中已有数据
    * */
    public static List<Student> init() {
        /*
         * 按照特定顺序，构造姓名、专业、分数三个数组，然后转换为Student列表
         * */
        String[] names = new String[]{
                "赵一", "李路", "王林",
                "钱小", "周舟", "冯楠",
                "孙飞", "吴同", "陈涛",
                "郑欢", "褚丽", "卫东"
        };

        Student.Gender[] genders = new Student.Gender[]{
                Gender.FEMALE, Gender.MALE, Gender.MALE,
                Gender.FEMALE, Gender.FEMALE, Gender.FEMALE,
                Gender.MALE, Gender.MALE, Gender.MALE,
                Gender.FEMALE, Gender.FEMALE, Gender.MALE
        };

        Student.Major[] majors = new Student.Major[]{
                Major.DM, Major.CS, Major.IoT,
                Major.CS, Major.IoT, Major.CS,
                Major.IoT, Major.DM, Major.AI,
                Major.AI, Major.DM, Major.AI
        };

        int[] scores = new int[]{
                81, 78, 84,
                88, 76, 54,
                86, 56, 68,
                68, 90, 87
        };

        // 使用Stream将四个数组合并为Student对象列表
        List<Student> students = IntStream.range(0, names.length).mapToObj(i ->
                new Student(names[i], genders[i], majors[i], scores[i])
        ).collect(Collectors.toList());

        // 打印学生信息
        students.forEach(student ->
                System.out.println(student.name + " - " + student.gender + " - " + student.major + " - " + student.score));

        return students;
    }


    public String getName() {
        return name;
    }

    public Gender getGender() {
        return gender;
    }

    public Major getMajor() {
        return major;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
}

