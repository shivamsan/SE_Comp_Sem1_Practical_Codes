#include <iostream>
using namespace std;
template <class T>
class sort
{
public:
 T a[50];
 int n;
 void accept()
 {
 cout << "Enter no. of elements: ";
 cin >> n;
 cout << "enter the elements: \n";
 for (int i = 0; i < n; i++)
 {
 cin >> a[i];
 }
 }
 void selection_sort()
 {
 T temp;
 for (int i = 0; i < n; i++)
 {
 for (int j = i + 1; j < n; j++)
 {
 if (a[i] > a[j])
 {
 temp = a[i];
 a[i] = a[j];
 a[j] = temp;
 }
 }
 }
 }
 void display()
 {
 for (int i = 0; i < n; i++)
 {
 cout << a[i] << "\t";
 }
 }
};
int main()
{
 int v;
 char ch;
 sort<int> s1;
 sort<float> s2;
 cout << "*****SELECTION SORT*******\n";
 do
 {
 cout << "-----sorting of integer and float array-----"
 << "\n";
 cout << "1.for int array\n";
 cout << "2.for float array\n";
 cout << "enter your choice: ";
 cin >> v;
 switch (v)
 {
 case 1:
 s1.accept();
 s1.selection_sort();
 cout << "\nSorted elements are:\n";
 s1.display();
 break;
 case 2:
 s2.accept();
 s2.selection_sort();
 cout << "\nSorted elements are:\n";
 s2.display();
 break;
 }
 cout << "\n_________________________________\n";
 cout << "\ndo you want to continue: ";
 cin >> ch;
 } while (ch == 'y' || ch == 'Y');
 return 0;
}