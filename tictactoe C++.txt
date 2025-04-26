#include <iostream>
#include <string>


using namespace std;

int main (){
    cout << " 2 player TICTACTOE " << endl;
    cout << "___________________________________________" << endl;
    cout << "___________________________________________" << endl;
    cout << "___________________________________________" << endl;
    cout << "        |         |         " << endl;
    cout << " (0 0)  | (0 1)   | (0 2)   " << endl;
    cout << "________|_________|________ " << endl;
    cout << " (1 0)  | (1 1)   | (1 2)   " << endl;
    cout << "________|_________|________ " << endl;
    cout << " (2 0)  | (2 1)   | (2 2)   " << endl;
    cout << "        |         |         " << endl;
    cout << "        |         |         " << endl;
    
    char board [3][3] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };
    
    const char playerX = 'X';
    const char playerO = '0';
    char currentPlayer = playerX;
    int r = -1;
    int c = -1;
    char winner = ' ';
    cout << "PLAYER X FIRST" << endl;
    for (int i = 0; i < 9; i++) {
        
    
        //print game board
    
        cout << "   |   |   " << endl;
        cout << " " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << endl;
        cout << "___|___|___" << endl;
        cout << "   |   |   " << endl;
        cout << " " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << endl;
        cout << "___|___|___" << endl;
        cout << "   |   |   " << endl;
        cout << " " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << endl;
        cout << "   |   |   " << endl;
        
        if (winner != ' '){
            break;
        }
        
        //player input
        
        cout << "Current Player is " << currentPlayer << endl;
        while (true) {
            cout << "Enter r c from 0-2 for row and column: ";
            cin >> r >> c;
            if ( r < 0 || r > 2 || c < 0 || c > 2) {
                cout << "Invalid input, try again " << endl;
            }
            else if (board[r][c] != ' ') {
                cout << "Tile is full, try again" << endl;
            }
            else {
                break;
            }
            r = -1;
            c = -1;
            
            cin.clear();
            cin.ignore(10000, '\n');
            
            
        }
      
        
        board[r][c] = currentPlayer;
        currentPlayer = (currentPlayer == playerX) ? playerO : playerX;
        
        for (int r = 0; r < 3; r++){
            if (board[r][0] != ' ' && board[r][0] == board [r][1] && board[r][1] == board[r][2]) {
                winner = board[r][0];
                break;
            }
        }
        
        for (int c = 0; c < 3; c++) {
            if (board[0][c] != ' ' && board[0][c] == board [1][c] && board[1][c] == board[2][c]) {
                winner = board[0][c];
            
            }
        }
        if (board[0][0] != ' ' && board [0][0] == board [1][1] && board[1][1] == board[2][2]){
            winner = board [0][0];
        }
        else if (board[0][2] != ' ' && board [0][2] == board [1][1] && board[1][1] == board[2][0]){
            winner = board [0][2];
        }
    }
    
    if (winner != ' '){
        cout << " PLayer " << winner << " is the winner " << endl;
    }
    else {
        cout << "Tie!" << endl;
    }
}
