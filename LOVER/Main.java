public class Main{
    public static void main(String[] args){

        char myChar = 'D';
        char myUnicodeChar = '\u0044';
        System.out.println(myChar);
        System.out.println(myUnicodeChar);
        char myCopyRightChar = '\u00A9';
        System.out.println(myCopyRightChar);


        String myString = "This is a String";
        System.out.println("myString is equal to " + myString);
        myString = myString + ", and this is more,";
        System.out.println("myString is equal to " + myString);
        myString = myString + "\u00A9 2019"; 
        System.out.println("myString is equal to " + myString);
        String numberString = "250.55";
        numberString = numberString + "49.95";
        System.out.println(numberString);
        String lastString = "10";
        int myInt = 50;
        lastString = lastString + myInt;
        System.out.println("LastString is equal to " + lastString);
        double doubleNumber = 120.47d;
        lastString = lastString + doubleNumber;
        System.out.println("LastString is equal to " + lastString);

        int result = 1 + 2;
        System.out.println("1 + 2 = " + result);
        int previousResult = result;
        System.out.println("previousResult = " + result);
    }
}