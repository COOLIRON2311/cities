#include<iostream>
#include<fstream>
#include<vector>


using namespace std;

int main()
{
	ofstream out;
	out.open("README.md");
	
	string word;
	vector<string> words;
	char c;
	
	out<<endl;
	
	while(cin>>c)
	{
		if(c=='l')
		{
			out<<endl;
		}
		else
		{
		cin.putback(c);
		cin>>word;
		out<<word<<" ";
	}
	}
	
	out<<endl;
	
	
	out.close();
	system("pause");
	return 0;
}
