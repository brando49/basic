#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
//类型
//std-标准，i-input，o-output
//ctrl+fn+f5运行快捷键
//char字符-1
//short短整型-2
//int整型-4
//long长整型-4，8
//long long更长整形-8
//float单精度浮点-4
//double双精度浮点-8
//int main()
//{
	//char ch = 'a';
	//printf("%c\n", ch);
	//int age = 20;
	//printf("%d\n", age);
	//float f = 3.1;
	//printf("%f\n", f);
	//long num1 = 100;
	//printf("%d\n", num1);
	//short num2 = 10;
	//printf("%d\n", num2);
	//double d = 3.14;
	//printf("%lf\n", d);
	//printf("%d%d\n", sizeof(short),sizeof(char));
	// 
	//int num1 = 0;
	//int num2 = 0;
	//int sum = 0;
	//scanf_s("%d%d", &num1, &num2);
	//sum = num1 + num2;
	//printf("sum= %d\n", sum);
//	return 0;
//}
//常量
	//const int a = 10;const修饰的常变量，本质还是变量，有常量属性
	//int a = 20;
	//printf("%d\n", a);
	//ctrlk+c注释选中行
	//int n = 10;
	//int arr[10] = { 0 };
	//printf("arr[10]");
//#define MAX 100
//#define str "abcdefg"
//int main()
//{
//	int a = MAX;
//	printf("%d\n", a);
//	printf("%s\n", str);
//	return 0;
//}//define定义标识符常量
//枚举常量不能改
//enum Color
//{
//	RED,
//	GREEN,
//	BLUE
//};枚举常量

//字符串
//int main()
//{
//	char arr[] = "hello,world";
//	char ars[] = { 'h','e','l','l','o',',','w','o','r','l','d' };
//	char art[] = { 'h','e','l','l','o',',','w','o','r','l','d','\0' };//'/0'是结束标准
//	printf("%s\n", arr);
//	printf("%s\n", ars);
//	printf("%s\n", art);
//	int len = strlen("abc");
//	printf("%d\n", len);
//	printf("%d\n", strlen(art));//利用strlen函数看不加\0的字符串实际长度，不算'\0'的长度
//	printf("%d\n", strlen(ars));
//	printf("%d\n", strlen(arr));
//	return 0;
//}

//转义字符
//int main()
//{
//	printf("abc\n");// \n换行
//	printf("abcn");
//	printf("are you ok\?\?)"); //??)-],??(-[
//	printf("%c\n",'\'');//\'让一个'可以被打印(\")
//	printf("abcd\\0ef");//\n是转义字符，让其可以被成功打印
//	printf("c:\\test\\test.c");//\t是制表符，等同于tab，再加个\
//	printf("abc\ndef");//\n换行
	/*
	int a = 10/*注释
	int b = 20
	*/
	//	return 0;
	//}

	//if-else语句
	//int main()
	//{
	//	int input = 0;
	//	printf("要加入比特\n");
	//	printf("要好好学习吗?\n");
	//	scanf("%d", &input);
	//
	//	if (input == 99)
	//	{
	//		printf("好offer\n");
	//	}
	//	else
	//	{
	//		printf("卖红薯\n");
	//	}
	//	return 0;
	//}

	//while语句
	//int main()
	//{
	//	int line = 0;
	//	printf("开始学习\n");
	//	while (line < 200)//括号内加判别式
	//	{
	//		printf("努力学习代码%d\n",line);
	//		line++;
	//	}
	//	
	//	if (line >= 200)
	//	{
	//		printf("成功了\n");
	//	}
	//	else
	//	{
	//		printf("继续加油\n");
	//	}
	//
	//
	//	return 0;
	//}

	//函数
	// 引入add函数求和
	//int Add(int x, int y)
	//{
	//	int z = 0;
	//	z = x + y;
	//	return z;
	//}
	//简化定义函数
	//int Add(int x, int y)
	//{
	//	return x + y;
	//}
	//int main()
	//{
	//	int a = 0;
	//	int b = 0;
	//	scanf_s("%d %d", &a, &b);
	//	int sum = Add(a,b);
	//	printf("%d\n", sum);
	//	return 0;
	//}

	//数组
	//int main()
	//{
	//	//int arr[10] = { 10,11,12,13,14,15,16,17,18,19 };
	//	//printf("%d\n", arr[8]);
	//	char arr1[] = { 'h','e','l','l','o',',','w','o','r','l','d','!'};
	//
	//	int i = 0;
	//	while (i < 12)
	//	{
	//		printf("%c", arr1[i]);
	//		i++;//等同于i=i+1
	//	}
	//		return 0;
	//}

	//比较大小
	//int max(int x, int y)
	//{
	//	if (x > y)
	//		return x;
	//	else
	//		return y;
	//}
	//int main()
	//{
	//	int a = 0;
	//	int b = 0;
	//	scanf_s("%d %d", &a, &b);
	//	int r = max(a, b);
	//	printf("%d\n", r);
	//
	//
	//	return 0;
	//}

	//输入大于0，返回-1；小于0，返回1；等于0，返回0 
	//int main()
	//{
	//	int x = 0;
	//	int y = 0;
	//	scanf_s("%d", &x);
	//	if (x > 0)
	//		y = -1;
	//	else if (x == 0)
	//		y = 0;
	//	else
	//		y = 1;
	//	printf("%d\n", y);
	//	return 0;
	//}

	// 也可以这么写（自己）
	//int  f(int x)
	//{
	//
	//	if (x == 0)
	//		return 0;
	//	else if (x < 0)
	//		return 1;
	//	else
	//		return -1;
	//}
	//int main()
	//{
	//	int a = 0;
	//	scanf_s("%d", &a);
	//	int y = f(a);
	//	printf("输出：%d", y);
	//	return 0;
	//}

	//操作符
	//除号和余号
	//int main()
	//{
	//	int a = 0;
	//	a = 7 / 2;
	//	printf("%d\n", a);//整形相除，只能得到整形
	//	float b = 0;
	//	b = 7.0 / 2;//要准确计算，两数至少有一个是浮点数
	//	printf("%.2f\n", b);//.nf表示取小数点后n位
	//	int c = 0;
	//	c = 7 % 2;
	//	printf("%d\n", c);//整形相除的余数，如7除2商3余1，得1
	//	return 0;
	//}
	//i=i+1>>i+=1,i=i-1>>ii_=1
	//

	//!表示相反，如0表示假，非0表示真，a=0，则!a为真
	//int main()
	//{
	//	int a = 0;
	//	if (!a)//括号内为a，则不会返回
	//	{
	//		printf("假\n");
	//	}
	//	return 0;
	//}

	//sizeof操作符，非函数，求某类型的字节大小
	//int main()
	//{
	//	int a = 10;
	//	printf("%d\n", sizeof a);//求整形a的大小
	//	printf("%d\n", sizeof(a));//也可以加括号
	//	printf("%d\n", sizeof (int));//求整形大小
	//	printf("%d\n", sizeof (float));
	//	printf("%d\n", sizeof (double));
	//	printf("%d\n", sizeof (char));
	//	return 0;
	//}
	//sizeof数组
	//int main()
	//{
	//	int arr1[10] = { 0 };
	//	printf("%d\n", sizeof(arr1));//求数组总共占用字节大小
	//	printf("%d\n", sizeof(arr1[0]));//求数组某一元素字节大小
	//	printf("%d\n", sizeof(arr1) / sizeof(int));//数组总占用大小除以单个类型元素占用大小，即求数组元素个数
	//	return 0;
	//}
	// a++与++a
	//int main()
	//{
	//	int a = 0;
	//	//int b = a++;//a先赋值给b，后++
	//	//printf("%d\n", a);
	//	//printf("%d\n", b);
	//	int b = ++a;//a先++，后赋值
	//	printf("%d\n", a);
	//	printf("%d\n", b);
	//	return 0;
	//}
	//强制转换
	//int main()
	//{
	//	int a = (int)3.14;//强制把f型转化为整形，去掉小数点
	//	printf("%d\n", a);
	//	return 0;
	//}
	//判别式==和赋值=
	//int main()
	//{
	//	int a = 10;
	//	if (a = 3)
	//	{
	//		printf("%d\n", a);//a=3是赋值，此时括号内已经没有真或假，而是直接赋值a=3，默认为真
	//	}
	//	if (a == 4)
	//	{
	//		printf("%d\n", a);//a==4是判断a是否为4，若为假则不返回
	//	}
	//	return 0;
	//}
	//逻辑和&&与逻辑或||
	//int main()
	//{
	//	int a = 0;
	//	int b = 0;
	//	//if (a && b)//&&判别左右两边均为真，有一方为假则均为假
	//	//{
	//	//	printf("真\n");
	//	//}
	//	if (a || b)//||判别左右两边至少有一边为真即为真
	//	{
	//		printf("假\n");
	//	}
	//	return 0;
	//}
	//条件操作符exp1 ? exp2 :exp3判别式exp1为真则执行exp2,否则执行exp3
	//int main()
	//{
	//	int a = 6;
	//	int b = 12;
	//	int c = a > b ? a : b;
	//	printf("%d\n", c);
	//	return 0;
	//}
	//逗号表达式
	//int main()
	//{
	//	int a = 1;
	//	int b = 2;
	//	int c = 3;
	//	int d = (a = 4 - b, b = 6 - a, c = 12 - a - b, 3 - 5);//逗号表达式的值按逗号依次改变，终值取最后一个表达式的值
	//	printf("%d\n", d);
	//	return 0;
	//}
	//[]操作符
	//int main()
	//{
	//	int arr[] = { 1,2,3,4,5,6,7,8,9,0 };//创建数组时，[]是表示数组内元素的个数
	//	int n = 3;
	//	arr[n] = 8;//更换元素时，[]是下标操作符
	//	printf("%d\n", arr[n]);
	//}

	//typedef函数改变变量名
	//typedef unsigned int uint;
	//typedef struct Node
	//{
	//	int data;
	//	struct Node* next;
	//}Node;
	//int main()
	//{
	//	unsigned int num = 0;
	//	uint num2 = 1;
	//	struct Node n;
	//	Node n2;
	//
	//	return 0;
	//}

	//static
	//void test()
	//{
	//	static int a = 1;//static的作用是保留前一个数据再使用该数据进行操作
	//	a++;
	//	printf(" %d", a);
	//}
	//
	//int main()
	//{
	//	int i = 0;
	//	while (i < 10)//从0开始，当i=0时执行test（），执行后对i进行+3，此时i=3，<10，可以继续执行，当a加到结果大于10时循环结束
	//	{
	//		test();
	//		i += 1;//当所赋值为小数时，自动选定整数，且不四舍五入;
	//	}
	//	return 0;
	//}

	//void??
	//void test()
	//{
	//	printf("Hello，world！");
	//	return 0;
	//}
	//int main()
	//{
	//	test();
	//	return 0;
	//}

	//extern申明外部变量
	//当从外部用extern引入变量时，若变量前加了static,则不能引用，即不能引用带static的变量
	//register建议电脑将数据放入寄存器中

	//#define add(x,y) (x+y)//define定义宏
	//int main()
	//{
	//	int a = 10;
	//	int b = 20;
	//	printf("%d\n", add(a, b));
	//}

	//指针与指针变量：指针就是通过地址来改变变量
	//指针就是地址，指针变量就是取、存放地址
	//int main()
	//{
		//int a = 10;
		//printf("%d\n", a);
		//int* p = &a;//取整形变量p为a的地址，p是指针变量
		//printf("%p\n", p);
		//*p = 20;//将地址p的数据重新赋值为20（前面已经规定p的类型是整形）
		//printf("%d\n", a);//此时对a的地址存放的数据改变导致a的改变
		// 暂时不会 
		//char ch = "H";
		//char* p = &ch;
		//printf("%c\n", ch);
		//printf("%p\n", p);
	//	return 0;
	//
	//}
	//
	// 输出商和余数
	//int main()
	//{
	//	int a = 0;
	//	int b = 0;
	//	scanf_s("%d %d", &a, &b);
	//	int c = a / b;
	//	int d = a % b;
	//	printf("%d %d\n", c, d);
	//	return 0;
	//}
	// 
	// struct结构体
	//struct Stu
	//{
	//	char name[20];
	//	int age;
	//	char sex[10];//括号内10表示有10个字符
	//	char tele[12];
	//};
	//void print(struct Stu* ps)
	//{
	//	printf("%s %d %s %s\n", (*ps).name, (*ps).age, (*ps).sex, (*ps).tele);
	//	printf("%s %d %s %s\n", ps->name, ps->age, ps->sex, ps->tele);
	//
	//
	//}
	//int main()
	//{
	//	struct Stu s = { "小明",18,"男","13333333333"};
	//	printf("%s %d %s %s\n", s.name, s.age, s.sex, s.tele);
	//	print(&s);
	//	return 0;
	//}



#include<stdio.h>

//
//struct Stu
//	{
//		char name[20];
//		int age;
//		char sex[10];//括号内10表示有10个字符
//		char tele[12];
//	};
//	void print(struct Stu* ps)
//	{
//		printf("%s %d %s %s\n", (*ps).name, (*ps).age, (*ps).sex, (*ps).tele);
//		printf("%s %d %s %s\n", ps->name, ps->age, ps->sex, ps->tele);
//	
//	
//	}
//	int main()
//	{
//		struct Stu s = { "小明",18,"男","13333333333"};
//		printf("%s %d %s %s\n", s.name, s.age, s.sex, s.tele);
//		print(&s);
//		return 0;
//	}

//void swap1(int& a, int& b)
//{
//	int c = a;
//	a = b;
//	b = c;
//}
//
//void swap2(int* a, int* b)
//{
//	int c = *a;
//	*a = *b;
//	*b = c;
//}
//
//int main()
//{
//	int a = 10, b = 5;
//	int* pa = &a, * pb = &b;
//	swap2(pa, pb);
//	printf("a=%d,b=%d\n", a, b);
//	return 0;
//}

//int main()
//{
//	int i = 0;
//	int arr[10] = { 1,2,3,4,5,6,7,8,9,10 };
//	for (i = 0; i <= 12; i++)
//	{
//		arr[i] = 0;
//		printf("hehe\n");
//	}
//	return 0;
//}
