#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
//����
//std-��׼��i-input��o-output
//ctrl+fn+f5���п�ݼ�
//char�ַ�-1
//short������-2
//int����-4
//long������-4��8
//long long��������-8
//float�����ȸ���-4
//double˫���ȸ���-8
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
//����
	//const int a = 10;const���εĳ����������ʻ��Ǳ������г�������
	//int a = 20;
	//printf("%d\n", a);
	//ctrlk+cע��ѡ����
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
//}//define�����ʶ������
//ö�ٳ������ܸ�
//enum Color
//{
//	RED,
//	GREEN,
//	BLUE
//};ö�ٳ���

//�ַ���
//int main()
//{
//	char arr[] = "hello,world";
//	char ars[] = { 'h','e','l','l','o',',','w','o','r','l','d' };
//	char art[] = { 'h','e','l','l','o',',','w','o','r','l','d','\0' };//'/0'�ǽ�����׼
//	printf("%s\n", arr);
//	printf("%s\n", ars);
//	printf("%s\n", art);
//	int len = strlen("abc");
//	printf("%d\n", len);
//	printf("%d\n", strlen(art));//����strlen����������\0���ַ���ʵ�ʳ��ȣ�����'\0'�ĳ���
//	printf("%d\n", strlen(ars));
//	printf("%d\n", strlen(arr));
//	return 0;
//}

//ת���ַ�
//int main()
//{
//	printf("abc\n");// \n����
//	printf("abcn");
//	printf("are you ok\?\?)"); //??)-],??(-[
//	printf("%c\n",'\'');//\'��һ��'���Ա���ӡ(\")
//	printf("abcd\\0ef");//\n��ת���ַ���������Ա��ɹ���ӡ
//	printf("c:\\test\\test.c");//\t���Ʊ������ͬ��tab���ټӸ�\
//	printf("abc\ndef");//\n����
	/*
	int a = 10/*ע��
	int b = 20
	*/
	//	return 0;
	//}

	//if-else���
	//int main()
	//{
	//	int input = 0;
	//	printf("Ҫ�������\n");
	//	printf("Ҫ�ú�ѧϰ��?\n");
	//	scanf("%d", &input);
	//
	//	if (input == 99)
	//	{
	//		printf("��offer\n");
	//	}
	//	else
	//	{
	//		printf("������\n");
	//	}
	//	return 0;
	//}

	//while���
	//int main()
	//{
	//	int line = 0;
	//	printf("��ʼѧϰ\n");
	//	while (line < 200)//�����ڼ��б�ʽ
	//	{
	//		printf("Ŭ��ѧϰ����%d\n",line);
	//		line++;
	//	}
	//	
	//	if (line >= 200)
	//	{
	//		printf("�ɹ���\n");
	//	}
	//	else
	//	{
	//		printf("��������\n");
	//	}
	//
	//
	//	return 0;
	//}

	//����
	// ����add�������
	//int Add(int x, int y)
	//{
	//	int z = 0;
	//	z = x + y;
	//	return z;
	//}
	//�򻯶��庯��
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

	//����
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
	//		i++;//��ͬ��i=i+1
	//	}
	//		return 0;
	//}

	//�Ƚϴ�С
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

	//�������0������-1��С��0������1������0������0 
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

	// Ҳ������ôд���Լ���
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
	//	printf("�����%d", y);
	//	return 0;
	//}

	//������
	//���ź����
	//int main()
	//{
	//	int a = 0;
	//	a = 7 / 2;
	//	printf("%d\n", a);//���������ֻ�ܵõ�����
	//	float b = 0;
	//	b = 7.0 / 2;//Ҫ׼ȷ���㣬����������һ���Ǹ�����
	//	printf("%.2f\n", b);//.nf��ʾȡС�����nλ
	//	int c = 0;
	//	c = 7 % 2;
	//	printf("%d\n", c);//�����������������7��2��3��1����1
	//	return 0;
	//}
	//i=i+1>>i+=1,i=i-1>>ii_=1
	//

	//!��ʾ�෴����0��ʾ�٣���0��ʾ�棬a=0����!aΪ��
	//int main()
	//{
	//	int a = 0;
	//	if (!a)//������Ϊa���򲻻᷵��
	//	{
	//		printf("��\n");
	//	}
	//	return 0;
	//}

	//sizeof���������Ǻ�������ĳ���͵��ֽڴ�С
	//int main()
	//{
	//	int a = 10;
	//	printf("%d\n", sizeof a);//������a�Ĵ�С
	//	printf("%d\n", sizeof(a));//Ҳ���Լ�����
	//	printf("%d\n", sizeof (int));//�����δ�С
	//	printf("%d\n", sizeof (float));
	//	printf("%d\n", sizeof (double));
	//	printf("%d\n", sizeof (char));
	//	return 0;
	//}
	//sizeof����
	//int main()
	//{
	//	int arr1[10] = { 0 };
	//	printf("%d\n", sizeof(arr1));//�������ܹ�ռ���ֽڴ�С
	//	printf("%d\n", sizeof(arr1[0]));//������ĳһԪ���ֽڴ�С
	//	printf("%d\n", sizeof(arr1) / sizeof(int));//������ռ�ô�С���Ե�������Ԫ��ռ�ô�С����������Ԫ�ظ���
	//	return 0;
	//}
	// a++��++a
	//int main()
	//{
	//	int a = 0;
	//	//int b = a++;//a�ȸ�ֵ��b����++
	//	//printf("%d\n", a);
	//	//printf("%d\n", b);
	//	int b = ++a;//a��++����ֵ
	//	printf("%d\n", a);
	//	printf("%d\n", b);
	//	return 0;
	//}
	//ǿ��ת��
	//int main()
	//{
	//	int a = (int)3.14;//ǿ�ư�f��ת��Ϊ���Σ�ȥ��С����
	//	printf("%d\n", a);
	//	return 0;
	//}
	//�б�ʽ==�͸�ֵ=
	//int main()
	//{
	//	int a = 10;
	//	if (a = 3)
	//	{
	//		printf("%d\n", a);//a=3�Ǹ�ֵ����ʱ�������Ѿ�û�����٣�����ֱ�Ӹ�ֵa=3��Ĭ��Ϊ��
	//	}
	//	if (a == 4)
	//	{
	//		printf("%d\n", a);//a==4���ж�a�Ƿ�Ϊ4����Ϊ���򲻷���
	//	}
	//	return 0;
	//}
	//�߼���&&���߼���||
	//int main()
	//{
	//	int a = 0;
	//	int b = 0;
	//	//if (a && b)//&&�б��������߾�Ϊ�棬��һ��Ϊ�����Ϊ��
	//	//{
	//	//	printf("��\n");
	//	//}
	//	if (a || b)//||�б���������������һ��Ϊ�漴Ϊ��
	//	{
	//		printf("��\n");
	//	}
	//	return 0;
	//}
	//����������exp1 ? exp2 :exp3�б�ʽexp1Ϊ����ִ��exp2,����ִ��exp3
	//int main()
	//{
	//	int a = 6;
	//	int b = 12;
	//	int c = a > b ? a : b;
	//	printf("%d\n", c);
	//	return 0;
	//}
	//���ű��ʽ
	//int main()
	//{
	//	int a = 1;
	//	int b = 2;
	//	int c = 3;
	//	int d = (a = 4 - b, b = 6 - a, c = 12 - a - b, 3 - 5);//���ű��ʽ��ֵ���������θı䣬��ֵȡ���һ�����ʽ��ֵ
	//	printf("%d\n", d);
	//	return 0;
	//}
	//[]������
	//int main()
	//{
	//	int arr[] = { 1,2,3,4,5,6,7,8,9,0 };//��������ʱ��[]�Ǳ�ʾ������Ԫ�صĸ���
	//	int n = 3;
	//	arr[n] = 8;//����Ԫ��ʱ��[]���±������
	//	printf("%d\n", arr[n]);
	//}

	//typedef�����ı������
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
	//	static int a = 1;//static�������Ǳ���ǰһ��������ʹ�ø����ݽ��в���
	//	a++;
	//	printf(" %d", a);
	//}
	//
	//int main()
	//{
	//	int i = 0;
	//	while (i < 10)//��0��ʼ����i=0ʱִ��test������ִ�к��i����+3����ʱi=3��<10�����Լ���ִ�У���a�ӵ��������10ʱѭ������
	//	{
	//		test();
	//		i += 1;//������ֵΪС��ʱ���Զ�ѡ���������Ҳ���������;
	//	}
	//	return 0;
	//}

	//void??
	//void test()
	//{
	//	printf("Hello��world��");
	//	return 0;
	//}
	//int main()
	//{
	//	test();
	//	return 0;
	//}

	//extern�����ⲿ����
	//�����ⲿ��extern�������ʱ��������ǰ����static,�������ã����������ô�static�ı���
	//register������Խ����ݷ���Ĵ�����

	//#define add(x,y) (x+y)//define�����
	//int main()
	//{
	//	int a = 10;
	//	int b = 20;
	//	printf("%d\n", add(a, b));
	//}

	//ָ����ָ�������ָ�����ͨ����ַ���ı����
	//ָ����ǵ�ַ��ָ���������ȡ����ŵ�ַ
	//int main()
	//{
		//int a = 10;
		//printf("%d\n", a);
		//int* p = &a;//ȡ���α���pΪa�ĵ�ַ��p��ָ�����
		//printf("%p\n", p);
		//*p = 20;//����ַp���������¸�ֵΪ20��ǰ���Ѿ��涨p�����������Σ�
		//printf("%d\n", a);//��ʱ��a�ĵ�ַ��ŵ����ݸı䵼��a�ĸı�
		// ��ʱ���� 
		//char ch = "H";
		//char* p = &ch;
		//printf("%c\n", ch);
		//printf("%p\n", p);
	//	return 0;
	//
	//}
	//
	// ����̺�����
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
	// struct�ṹ��
	//struct Stu
	//{
	//	char name[20];
	//	int age;
	//	char sex[10];//������10��ʾ��10���ַ�
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
	//	struct Stu s = { "С��",18,"��","13333333333"};
	//	printf("%s %d %s %s\n", s.name, s.age, s.sex, s.tele);
	//	print(&s);
	//	return 0;
	//}
