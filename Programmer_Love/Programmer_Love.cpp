#include <iostream>
using namespace std;

int i = 1;
int alive = 1;

class MyWords {
public:
    void to(string you) {
        while (i == alive) {
            cout << "  I love " << you << " :)" << endl;
        }
    }
};

int main() {
    MyWords obj;
    obj.to("You");
    return 0;
}

