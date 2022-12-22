#include<iostream>
using namespace std;
class stack
{
 public:
const static int size = 100;
 int top =-1;
 char array[size];
 void push(char x)
 {
 if(top==size-1)
 {
 cout<<"\nstack overflow";
 return;
 }
 array[++top]= x;
 }
 char pop()
 {
 if(top==-1)
 {
 cout<<"\nstack underflow";
 return -1;
 }
 return array[top--];
 }
 void display()
 {
 if(top==-1){
 cout<<"\nstack is empty";
 }
 cout<<"\nstack contains : ";
 for(int i=0;i<=top;i++)
 {
 cout<<array[i]<<" ";
 }
 cout<<endl;
 }
};
int main()
{
 stack s;
 string userip;
 cout<<"\nEnter a string: ";
 getline(cin,userip);
 string orgstr=" ";
 for(int i=0;i<=userip.size();i++)
 {
 char ch= userip[i];
 if(ch>='a' and ch <='z')
 {
 ch=(char)(ch-'a'+'A');
 }
 if(ch>='A' and ch<='Z')
 {
 s.push(ch);
 orgstr.push_back(ch);
 }
 }
 cout<<"Original string: "<<orgstr<<endl;
 string revstr=" ";
 while(s.top!=-1)
 {
 revstr.push_back(s.pop());
 }
 cout<<"Reversed string: "<<revstr<<endl;
 bool is_palindrome=true;
 for(int i=0;i<=orgstr.size();i++)
 {
 if(orgstr[i]!=revstr[i])
 {
 is_palindrome=false;
 break;
 } 
 }
 cout<<userip<<" is"<<(is_palindrome?" ":" not")<<" a palindrome."<<endl;
}