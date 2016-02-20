import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
SRC_DIR = os.path.join(BASE_DIR, 'src')
Q_DIR = os.path.join(BASE_DIR, 'questions')

GIT_BASE_URL = 'https://github.com/SivaPandeti/python-interview/blob/master/src'

if not os.path.exists(Q_DIR):
  os.makedirs(Q_DIR)

for folder_name in os.listdir(SRC_DIR):
  with open(os.path.join(Q_DIR, '{}.md'.format(folder_name)), 'w') as of:
    toc = ['# Questions']
    i = 1
    contents = []
    for filename in os.listdir(os.path.join(SRC_DIR, folder_name)):
      problem = ' '.join([w.capitalize() for w in filename.replace('.py', '').split('_')])
      problem_link = '#' + '-'.join([w for w in filename.replace('.py', '').split('_')])
      toc.append('{}. [{}]({})'.format(i, problem, problem_link))
      with open(os.path.join(SRC_DIR, folder_name, filename), 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.startswith('##')]
      formatted_lines = ['## ' + problem]
      formatted_lines += [line[5:] if line.startswith('##   ') else '#' + line for line in lines]
      formatted_lines += [' ']
      solution = '### Solution\n[click here]{}/{}/{}\n'.format(GIT_BASE_URL, folder_name, filename)
      contents.append('\n'.join(formatted_lines) + solution)
      i += 1
    of.write('\n'.join(toc) + '\n\n')
    of.write('\n'.join(contents))
