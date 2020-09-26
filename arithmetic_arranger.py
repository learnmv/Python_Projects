class operator_error(Exception):
  pass
class alphabet_error(Exception):
  pass
class length_error(Exception):
  pass
class too_many_error(Exception):
  pass

def sol(p1,p2,p3):
  x1=len(p1)
  x2=len(p3)
  new = ""
  if ('+' in p2):
    y = int(p1) + int(p3)
    x3 = len(str(y))
  elif('-' in p2):
    y = int(p1) - int(p3)
    x3 = len(str(y))
  if x1 > x2:
    new = ' '*(x1-x3+2)+str(y)
  elif x2 > x1:
    new = ' '*(x2-x3+2)+str(y)
  else:
    new = ' '*(x1-x3+2)+str(y)
  return new

def arithmetic_arranger(problems,solution = False):
  try:
    if len(problems)>5:
      raise too_many_error('')
    op1 = []
    op2 = []
    op3 = []
    sol1 = []
    for problem in problems:
      l1 = problem.split(' ')
      x1 = len(l1[0])
      x2 = len(l1[2])
      if (l1[1] not in ['+','-']):
        raise operator_error('')
      elif not(l1[0].isdigit()):
        raise alphabet_error('')
      elif not(l1[2].isdigit()):
        raise alphabet_error('')
      elif (x1>4) or (x2>4):
        raise length_error('')

      if (x1 > x2):
        op1.append('  '+l1[0])
        op2.append(l1[1]+' '+(' '*(x1-x2))+l1[2])
        op3.append('-'*(x1+2))
        if solution:
          sol1.append(sol(l1[0],l1[1],l1[2]))
      elif (x2 > x1):
        op1.append((' '*(x2-x1+2))+l1[0])
        op2.append(l1[1]+' '+l1[2])
        op3.append('-'*(x2+2))
        if solution:
          sol1.append(sol(l1[0],l1[1],l1[2]))
      else:
        op1.append((' '*2) + l1[0])
        op2.append(l1[1]+' '+l1[2])
        op3.append('-'*(x1+2))
        if solution:
          sol1.append(sol(l1[0],l1[1],l1[2]))
    line1 = '    '.join(op1)
    line2 = '    '.join(op2)
    line3 = '    '.join(op3)
    if solution:
      line4 = '    '.join(sol1)
      return line1+'\n'+line2+'\n'+line3+'\n'+line4
    else:
     return line1+'\n'+line2+'\n'+line3
  except operator_error:
    return "Error: Operator must be '+' or '-'."
  except alphabet_error:
    return "Error: Numbers must only contain digits."
  except length_error:
    return "Error: Numbers cannot be more than four digits."
  except too_many_error:
    return "Error: Too many problems."
