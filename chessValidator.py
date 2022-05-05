#! python3
#-*- coding: utf-8 -*-

#Данная программа будет проверять на правильность ходы в шахматах
chessBoard = {'lh' : 'bking' , '6с': 'wqueen', '2g' : 'bbishop', '5h' : 'bqueen' , '3e' : 'wking'}

def isValidChessBoard(move):
    bKing, wKing, bPieces, wPieces = 0, 0, 0, 0
    bPawns, wPawns, spaces, check = 0, 0, [], True
    horizontallLine = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    for x in (horizontallLine):
        for y in range (1,9):
            spaces.append(x + str(y))
    for space, pieces in chessBoard.items():
        if space not in spaces:
            check = False
        if pieces == 'wKing':
            wKing += 1
        if pieces == 'bKing':
            bKing += 1
        if pieces == 'wPawns':
            wPawns += 1
        if pieces == 'bPawns':
            bPawns += 1
        if pieces.startswith('w'):
            wPieces += 1
        if pieces.startswith('b'):
            bPieces += 1
    if wKing != 1:
        check = False
    if bKing != 1:
        check = False
    if wPawns > 8:
        check = False
    if bPawns > 8:
        check = False
    if bPieces > 16:
        check = False
    if wPieces > 16:
        check = False
    if check:
        return True
    else:
        return False
print(isValidChessBoard(chessBoard))



#Моя проблема: я не могу придумать код. Я его могу прочитать, но придумать не могу
# Надо подумать над описанием и названием переменных