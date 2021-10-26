# -*- coding: utf-8 -*-
"""ai-a3-2019459.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-5vQA-IS-TFN_s4jYMYtPmZBpxZfkXB
"""

pip install durable-rules

from durable.lang import *

with ruleset('system'):
  @when_all((m.field == 'AI'), (m.interest == 'math'))
  def prospect(c):
    c.assert_fact({'prospect': 'ML'})
  
  @when_all((m.field == 'AI'), (m.type == 'theory'))
  def course(c):
    c.assert_fact({'course': 'AI'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Artificial Intelligence'})
  
  @when_all((m.prospect == 'ML'), (m.interest == 'language'))
  def course(c):
    c.assert_fact({'course': 'NLP'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Natural language processing'})
  
  @when_all((m.field == 'AI'), (m.interest == 'visuals'))
  def course(c):
    c.assert_fact({'course': 'CV'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Computer vision'})
  
  @when_all((m.field == 'CS'), (m.type == 'theory'))
  def prospect(c):
    c.assert_fact({'prospect': 'coreCS'})
  
  @when_all((m.prospect == 'coreCS'))
  def course(c):
    c.assert_fact({'course': 'ADA'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Analysis and design of algorithms'})
  
  @when_all((m.prospect == 'coreCS'))
  def course(c):
    c.assert_fact({'course': 'DBMS'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Database management system'})
  
  @when_all((m.prospect == 'coreCS'), (m.interest == 'network'))
  def course(c):
    c.assert_fact({'course': 'CN'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Computer networks'})
  
  @when_all((m.field == 'CS'), (m.interest == 'problem-solving'))
  def course(c):
    c.assert_fact({'course': 'DSA'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Data structures and algorithms'})
  
  @when_all((m.prospect == 'coreCS'), (m.interest == 'problem-solving'), (m.interest == 'math'))
  def activity(c):
    c.assert_fact({'activity': 'CP'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Competitive programming'})
  
  @when_all((m.field == 'ECA'), (m.interest == 'language'))
  def activity(c):
    c.assert_fact({'activity': 'debate'})
    c.assert_fact({'activity': 'writing'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Debating'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Writing'})
  
  @when_all((m.field == 'ECE'), (m.interest == 'hardware'))
  def activity(c):
    c.assert_fact({'activity': 'robotics'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Robotics'})
  
  @when_all((m.field == 'ECE'), (m.interest == 'visuals'))
  def course(c):
    c.assert_fact({'course': 'DIP'})
    c.assert_fact('output', {'subject': 'take', 'predicate': 'course', 'object': 'Digital Image Processing'})
  
  @when_all((m.field == 'design'), (m.interest == 'visuals'))
  def prospect(c):
    c.assert_fact({'prospect': 'designer'})
  
  @when_all((m.prospect == 'designer'), (m.interest == 'art'))
  def activity(c):
    c.assert_fact({'activity': 'graphics'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Graphic design'})
  
  @when_all((m.prospect == 'designer'), (m.interest == 'video'))
  def activity(c):
    c.assert_fact({'activity': 'videos'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Video editing'})
  
  @when_all((m.field == 'design'), (m.interest == 'webdev'))
  def activity(c):
    c.assert_fact({'activity': 'frontend'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Front-end developer'})
  
  @when_all((m.course == 'DBMS'), (m.interest == 'webdev'))
  def activity(c):
    c.assert_fact({'activity': 'backend'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Back-end developer'})
  
  @when_all((m.activity == 'frontend'), (m.activity == 'backend'))
  def activity(c):
    c.assert_fact({'activity': 'fullstack'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Full-stack developer'})
  
  @when_all((m.field == 'ECA'), (m.type == 'performative'))
  def activity(c):
    c.assert_fact({'activity': 'dance'})
    c.assert_fact({'activity': 'drama'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Dancing'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Theatre'})
  
  @when_all((m.field == 'ECA'), (m.type == 'competitive'))
  def prospect(c):
    c.assert_fact({'prospect': 'sports'})
  
  @when_all((m.prospect == 'sports'), (m.type == 'physical'))
  def activity(c):
    c.assert_fact({'activity': 'football'})
    c.assert_fact({'activity': 'basketball'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Football'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Basketball'})
  
  @when_all((m.prospect == 'sports'), (m.type == 'non-physical'))
  def activity(c):
    c.assert_fact({'activity': 'chess'})
    c.assert_fact('output', {'subject': 'try', 'predicate': 'activity', 'object': 'Chess'})
  
  @when_all(+m.course)
  def output(c):
    pass
  
  @when_all(+m.activity)
  def output(c):
    pass
  
  @when_all(+m.interest)
  def output(c):
    pass
  
  @when_all(+m.type)
  def output(c):
    pass
  
  @when_all(+m.prospect)
  def output(c):
    pass

with ruleset('output'):
  @when_all(+m.subject)
  def output(c):
    print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

fl = ['CS', 'ECE', 'AI', 'design', 'ECA']
il = ['math', 'language', 'visuals', 'network', 'problem-solving', 'hardware', 'art', 'video', 'webdev']
tl1 = ['theory', 'performative', 'competitive']
tl2 = ['physical', 'non-physical']

def fieldinput():
  fields = []
  print('\nChoose the fields you would like to explore\nEnter corresponding numbers line by line\nEnter end to stop input\n)')
  for i in range(len(fl)):
    print(i+1, fl[i])
  while(True):
    temp = input()
    if(temp=='end'):
      break
    else:
      fields.append(fl[int(temp) - 1])
  return fields

def interestinput():
  interests = []
  print('\nChoose the topics you are interested in\nEnter corresponding numbers line by line\nEnter end to stop input\n)')
  for i in range(len(il)):
    print(i+1, il[i])
  while(True):
    temp = input()
    if(temp=='end'):
      break
    else:
      interests.append(il[int(temp) - 1])
  return interests

def typeinput():
  types = []
  print('\nChoose your preferred type of course and activitiy\nEnter corresponding numbers line by line\nEnter end to stop input)')
  for i in range(len(tl1)):
    print(i+1, tl1[i])
  while(True):
    temp = input()
    if(temp=='end'):
      break
    else:
      types.append(tl1[int(temp) - 1])
  
  if('competitive' in types):
    print('\nChoose your preferred type of sport\nEnter corresponding numbers line by line\nEnter end to stop input)')
    for i in range(len(tl2)):
      print(i+1, tl2[i])
    while(True):
      temp = input()
      if(temp=='end'):
        break
      else:
        types.append(tl2[int(temp) - 1])
  return types

def takeinput():
  fields = fieldinput()
  interests = interestinput()
  types = typeinput()
  return fields, interests, types

f, i, t = takeinput()
print()
for x in f:
  assert_fact('system', {'field': x})
for x in i:
  assert_fact('system', {'interest': x})
for x in t:
  assert_fact('system', {'type': x})

print('Suggested courses and activities -\n')
system = get_facts('system')
for rule in system:
  if 'course' in rule:
    print('course:', rule['course'])
  elif 'activity' in rule:
    print('activity:', rule['activity'])



"""Prewritten assertions below.
Instead of giving input try these to see how the rules are satisfied as new facts are provided
"""

assert_fact('system', {'field': 'AI'})
assert_fact('system', {'interest': 'math'})
assert_fact('system', {'type': 'theory'})
assert_fact('system', {'interest': 'language'})

assert_fact('system', {'field': 'CS'})

assert_fact('system', {'interest': 'network'})

assert_fact('system', {'interest': 'webdev'})
assert_fact('system', {'interest': 'problem-solving'})