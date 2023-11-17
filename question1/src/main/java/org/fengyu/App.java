package org.fengyu;

import org.fengyu.model.Student;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) throws IOException {
        // 问题 1
        int[] scores = getScores();

        // 问题 2
        System.out.println("********** Scores **********");
        printScores(scores);

        // 问题 3
        double[] stats = calculateStats(scores);
        System.out.println("********** Stats ***********");
        System.out.println("Mean: " + stats[0]);
        System.out.println("Range: " + stats[1]);
        System.out.println("Standard Deviation: " + stats[2]);

        // 问题 4
        System.out.println("********** Students **********");
        List<Student> students = Student.init();

        // 问题 5
        System.out.println("********Female Students with Score >= 80********");
        filterAndPrintFemaleStudents(students);

        // 问题 6
        swapScoresAndSaveToFile(students);

    }


    /*
     * 问题 1 请选择合理的数据类型，构建数组（或列表），完成对上述同学的分数记录。
     * */
    private static int[] getScores() {
        int[] scores = new int[]{
                81, 78, 84, 88, 76, 54, 86, 56, 68, 68, 90, 87
        };
        return scores;
    }

    /*
     * 问题 2 请使用循环结构将上述同学分数的记录数组（或列表）输出显示。
     * */
    private static void printScores(int[] scores) {
        for (int i = 0; i < scores.length; i++) {
            System.out.println(scores[i]);
        }
    }

    /*
     * 问题 3 请设计一个函数，将上述分数数组（或列表）作为实参传入，并对分数数组进行平均值，极差，标准差进行求解，以返回值的形式得到结果并显示。
     * */
    public static double[] calculateStats(int[] scores) {
        double sum = 0; // 用于累加分数，计算平均值
        int maxScore = Integer.MIN_VALUE; // 初始最大值设为可能的最小整数，用于找出最高分
        int minScore = Integer.MAX_VALUE; // 初始最小值设为可能的最大整数，用于找出最低分

        // 遍历分数数组，计算总和，并找出最大值和最小值
        for (int score : scores) {
            sum += score; // 累加分数
            if (score > maxScore) maxScore = score; // 更新最大分数
            if (score < minScore) minScore = score; // 更新最小分数
        }

        double mean = sum / scores.length; // 计算平均值

        double variance = 0; // 初始化方差
        // 计算方差
        for (int score : scores) {
            variance += Math.pow(score - mean, 2); // 累加每个分数与平均值差的平方
        }
        variance /= scores.length; // 将累加的总和除以分数的数量，得到方差

        double stdDeviation = Math.sqrt(variance); // 计算标准差，即方差的平方根
        double range = maxScore - minScore; // 计算极差，即最大分数和最小分数之差

        return new double[]{mean, range, stdDeviation}; // 返回包含平均值、极差和标准差的数组
    }


    /*
     * 问题 5 请使用分支结构筛选出你所构建的数据类型数组中，女性成员中分数大于等于 80 分的同学，输出其姓名和专业。
     * */
    public static void filterAndPrintFemaleStudents(List<Student> students) {
        for (Student student : students) {
            if (student.getGender() == Student.Gender.FEMALE && student.getScore() >= 80) {
                System.out.println(student.getName() + " - " + student.getMajor());
            }
        }
    }



    /*
    * 问题 6 由于记录人员疏忽，物联网、智科两专业的最高分同学分数颠倒，
    * 请使用指针的形式（C 语言必须，其他语言可不使用指针）完成上述两个专业最
    * 高分同学成绩的互换，并把最终每个专业最高分的同学信息形成一个文本，以文件的形式保存下来。
    * */
    public static void swapScoresAndSaveToFile(List<Student> students) throws IOException {
        Student maxIoTStudent = null;
        Student maxAIStudent = null;

        // 找到物联网和智科两个专业的最高分学生
        for (Student student : students) {
            if (student.getMajor() == Student.Major.IoT && (maxIoTStudent == null || student.getScore() > maxIoTStudent.getScore())) {
                maxIoTStudent = student;
            } else if (student.getMajor() == Student.Major.AI && (maxAIStudent == null || student.getScore() > maxAIStudent.getScore())) {
                maxAIStudent = student;
            }
        }

        // 交换两个专业最高分学生的分数
        if (maxIoTStudent != null && maxAIStudent != null) {
            int tempScore = maxIoTStudent.getScore();
            maxIoTStudent.setScore(maxAIStudent.getScore());
            maxAIStudent.setScore(tempScore);

            // 将结果保存到文件
            try (FileWriter writer = new FileWriter("highest_scores.txt")) {
                writer.write("IoT Highest Score: " + maxIoTStudent.getName() + " - " + maxIoTStudent.getScore() + "\n");
                writer.write("AI Highest Score: " + maxAIStudent.getName() + " - " + maxAIStudent.getScore() + "\n");
                System.out.println("Highest scores saved to file.");
            }
        }
    }


}
