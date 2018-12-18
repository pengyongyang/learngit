#! /usr/bin/env  python3
# -*- coding:utf-8 -*-

class Huang:
	def __init__(self):
		self.student=['peng','lan','tang','qi','zhang']
	def show_student(self):
		for student in self.student:
			print(student)

class b103(Huang):
	def __init__(self):
		super().__init__()
		self.people=self.student+['chen','liu','wei','li','khalid']
	def show_people(self):
		for people in self.people:
			print(people)


if __name__ == "__main__":
	b_103=b103()
	b_103.show_people()
