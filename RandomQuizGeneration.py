#! Python3

# RandomQuizGenerator - ��� ���

import random

capitals = {'A��a�o': '�e��p �o�ce', 'A�o�a': 'Oc�o��o� �e��p �e-Mo��', 'A�a�ama': 'Mo���omep�', 'A��cka': '�e��p ��y�o', 'Ap��o�a': 'C�o������ pa�o� ����kc', 'Apka��ac': '����-pok', '�a�om���': '�a�e�', '�a�����o�': 'O��m���', '�epmo��': 'Mo������ep', '��p�����': 'P��mo��', '��p����� �a�a��a�': '�ap�c�o�', '��cko�c��': 'C�o������ pa�o� M���co�', '�a�a��': '�e��p �o�o�y�y', '�ako�a Ce�ep�a�': '�e��p ��cmapk', '�ako�a ���a�': '�e��p ��pp', '�e�a��p': '�o�ep', '��op����': '�e��p A��a��a', '�����o�c': 'C�p�������', '����a�a': '�e��p ����a�a�o��c', 'Ka���op���': 'Cakpame��o', 'Ka��ac': 'To��ka', 'Kapo���a Ce�ep�a�': 'Po��', 'Kapo���a ���a�': '�e��p Ko�ym���', 'Ke��ykk�': '�e��p �pa�k�op�', 'Ko�opa�o': '�e��p �e��ep', 'Ko��ek��ky�': 'Oc�o��o� pa�o� �ap��op�', '�y���a�a': '�e��p �a�o�-Py�', 'Macca�yce�c': '�e��p �oc�o�', 'M���eco�a': 'Ce�-�o�', 'M�cc�c���': '���kco�', 'M�ccyp�': '���e��epco�-C���', 'M����a�': '�e��p �a�c���', 'Mo��a�a': '�e�e�a', 'M��': '�e��p O�ac�a', 'M�p��e��': 'C�o������ pa�o� A��a�o��c', '�e�packa': '�e��p ���ko���', '�e�a�a': 'Kapco�-C���', '��m���p': 'Ko�kop�', '��epc�': 'Tpe��o�', '�opk': '�e��p O��a��', 'Mekc�ko': 'Ca��a-�e', 'O�a�o': 'Ko�ym�yc', 'Ok�a�oma': 'Ok�a�oma-c���', 'Ope�o�': 'C�o������ pa�o� Ce��em', '�e�c����a���': '�app�c�ep�', 'A��e��': '�po���e�c', 'Te��ec�': '�e��p �������', 'Te�ac': '�e��p oc���', '��op��a': '�e��p Ta��a�acc�', '��a': 'C�o���a pa�o� Co��-�e�k-C���'}
#  TODO: ������� ����� ������� � ������ �������
for quiznum in range(35):
    #  �������� ������, ������� � ������ �������
    quizfile = open('capitalsquiz%s.txt' % (quiznum + 1), 'w')
    answerkeyfile = open('capitalquiz_answers%s.txt' % (quiznum + 1), 'w')
    #  ������ ��������� ������
    quizfile.write('���:\n\n����:\n\n�����:\n\n')
    quizfile.write((' ' * 15) + '�������� ������ ������ ������ (����� %s)' % (quiznum + 1))
    quizfile.write('\n\n')
    #  �������������� ������� ���������� ������ ������
    states = list(capitals.keys())
    random.shuffle(states)
#  TODO: �������� ��������� ������

#  TODO: ���������� ������� ���������� �������

#  TODO: ������������ ���� �� ���� 50 ������,
#  �������� ������ ��� ������� �� ���
