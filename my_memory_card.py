from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
 
 
app = QApplication([])
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
       
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
   
def end_screen():
    btn_OK.setText('Выйти')
    RadioGroupBox.hide()
    AnsGroupBox.hide()
    lb_Result.hide()
    lb_Question.hide()
    score = window.score / len(questions_list) * 100
    end_Label = QLabel(f'Поздравляем! Ваш результат: {round(score, 2)}% ')
    layout_line2.addWidget(end_Label, alignment=Qt.AlignCenter)  
 
def show_result():
    if answers[0].isChecked():
        lb_Result.setText('Правильно!')
        window.score += 1
        lb_Correct.setText('')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        lb_Result.setText('Неправильно!')
        lb_Correct.setText(answers[0].text())
    RadioGroupBox.hide()
    AnsGroupBox.show()
    window.index += 1
    print(window.index)
    if window.index == len(questions_list):
        btn_OK.setText('Завершить')
    else:
        btn_OK.setText('Следующий вопрос')
   
 
def show_question():
    ask(questions_list[window.index])
    print(window.index)
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
 
def test():
    if btn_OK.text()=='Ответить':
        show_result()
    elif btn_OK.text() == 'Завершить':
        end_screen()
    elif btn_OK.text() == 'Выйти':
        window.close()
    else:
        show_question()
 
btn_OK = QPushButton('Приступить')
 
btn_OK.clicked.connect(test)
 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов")
 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()  
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1)
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)  
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
RadioGroupBox.hide()
AnsGroupBox.show()
 
questions_list = []
 
questions_list.append(Question('В каком году был 200 год','200','201','202','203'))
questions_list.append(Question('В каком году был 100 год','100','101','102','103'))
questions_list.append(Question('Сколько букв в слове \"один\"', '4', '2', '3', '1'))
 
shuffle(questions_list)
 
 
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.show()
window.index = 0
window.score = 0
app.exec()

