## Function


### 1. **Basic Structure of a Function**

In C#, a function usually looks something like this:

```csharp
returnType FunctionName(parameter1Type parameter1, parameter2Type parameter2, ...)
{
    // Code to execute
    return returnValue;
}
```

- **ReturnType**: The type of value the function returns. If the function does not return a value, this is specified as `void`.
- **FunctionName**: The name of the function, following naming conventions.
- **Parameters**: The inputs to the function, specified with types and names. A function can have zero or more parameters.
- **Return Value**: The value returned by the function. If the return type is `void`, no value is returned.

### 2. **Types of Functions**

#### **Void Functions**
These functions do not return a value. They are used when you need to execute a block of code but don't need to send any data back. For example, a function that prints a message on the screen might not need to return anything.

```csharp
void DisplayMessage()
{
    Console.WriteLine("Hello, world!");
}
```

### **Static Keyword**

- The static keyword in C# designates a class member that is associated with the class itself rather than any individual instance.
- Static functions, therefore, **can be called on the class and not on objects of the class**. 
- These functions can only interact with other static members and are particularly useful for creating utility functions that perform general tasks, like calculations, which don't rely on instance-specific data.
- Due to their nature, static methods are stored in memory only once, which enhances memory efficiency, especially in applications with numerous instances of a class.
-  if a function in C# is not declared with the static keyword, it means that the function is an instance method. Instance methods require you to create an object of the class to call them because they can operate on and modify data contained within a specific instance of the class.
 ```c#

 //using static keyword
 class Calculator
 {
     // A static method to add two numbers
     public static int Add(int num1, int num2)
     {
         return num1 + num2;
     }
 }
 static void Main(string[] args)
 {


 // Calling the static method on the class without creating an instance
     int result = Calculator.Add(5, 3);
     Console.WriteLine("Sum: " + result);
     Console.ReadLine();

 }

 //without using static keyword you should make instance 
    class Calculator
{
    // An instance method to add two numbers
    public int Add(int num1, int num2)
    {
        return num1 + num2;
    }
}
static void Main(string[] args)
{


    // Creating an instance of the Calculator class
    Calculator myCalculator = new Calculator();
    // Calling the instance method on the object
    int result = myCalculator.Add(5, 3);
    Console.WriteLine("Sum: " + result);

    Console.ReadLine();

}
```
#### **Value-Returning Functions**
These functions perform operations and then return a value. For instance, a function that adds two numbers and returns the result:

```csharp
int Add(int num1, int num2)
{
    return num1 + num2;
}
```

### 3. **Parameter Types**

#### **Default Parameter**
```c#
// default parameter
static void info(string fname = "Rakwan", string lname = "Ali")
{
    Console.WriteLine("full name is : " + fname + " " + lname);
}
static void Math(int x, int y)
{
    Console.WriteLine(x + y);
}
static void Main(string[] args)
{
    Math(5, 5);
    info();
    Console.ReadLine();
}
```

#### **Reference Parameters (`ref` Keyword)**
When you pass parameters by reference using the `ref` keyword, the function can modify the original data directly. This is useful when you want the function to update the values of the passed arguments.

```csharp
void Increment(ref int number)
{
    number += 1;
}
```

#### **Output Parameters (`out` Keyword)**
Output parameters are similar to reference parameters, but they are used when a function needs to return more than one value.

```csharp
void GetValues(out int val1, out int val2)
{
    val1 = 10;
    val2 = 20;
}
```

#### **Parameter Arrays (`params` Keyword)**
Sometimes you might want to pass an unknown number of parameters to a function. C# allows this with the `params` keyword, which lets you pass a comma-separated list of arguments of the same type.

```csharp
int Add(params int[] numbers)
{
    int sum = 0;
    foreach (int num in numbers)
    {
        sum += num;
    }
    return sum;
}
```


### 5. **Function Overloading**
Function overloading allows multiple functions with the same name but different parameters (different type or number of parameters). This is useful for creating functions that do similar things but with different types of inputs.

```csharp
int Multiply(int x, int y)
{
    return x * y;
}

double Multiply(double x, double y)
{
    return x * y;
}
```

### 6. **Lambda Expressions**
These are a concise way to represent anonymous methods. Lambda expressions are useful for short snippets of code that are passed to functions that accept delegates or for use with LINQ queries.

```csharp
List<int> numbers = new List<int> { 1, 2, 3, 4 };
int sum = numbers.FindAll(x => x > 2).Sum();
```

### Conclusion
Functions in C# are versatile tools that help you organize and manage your code effectively. They can perform tasks ranging from simple actions like displaying messages to complex calculations and data processing. Understanding how to use different types of functions and parameters will greatly enhance your ability to write robust and maintainable C# applications.

