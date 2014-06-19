#!/usr/local/bin/python3.3
#encoding: utf-8
'''
demo -- shortdesc

demo is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2014 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

class Animal(object):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.stomach = []        
 
    def __call__(self,food):
        self.stomach.append(food)
 
    def poop(self):
        if len(self.stomach) > 0:
            return self.stomach.pop(0)
 
    def __str__(self):        
        return 'A animal named %s' % (self.name)       
 
cow = Animal('king', 4)  #We make a cow
dog = Animal('flopp', 4) #We can make many animals
print('我们有两个动物， 牛的名字叫  %s ，狗的名字叫  %s, 总共有 %s 条腿.end' % (cow.name, dog.name, cow.legs))
print(cow)  #here __str__ metod work
 
#We give food to cow
cow('gras')
print(cow.stomach)
 
#We give food to dog
dog('bone')
dog('beef')
print(dog.stomach)
 
#What comes inn most come out
print(cow.poop())
print(cow.stomach)  #Empty stomach
 
'''-->output
We have 2 animales a cow name king and dog named flopp,both have 4 legs
A animal named king
['gras']
['bone', 'beef']
gras
[]
'''