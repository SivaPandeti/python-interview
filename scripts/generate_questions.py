import os

BASE_DIR = os.path.dirname(os.getcwd())
SRC_DIR = os.path.join(BASE_DIR, 'src')
Q_DIR = os.path.join(BASE_DIR, 'questions')

if not os.path.exists(Q_DIR):
  os.makedirs(Q_DIR)

for folder_name in os.listdir(SRC_DIR):
  with open(os.path.join(Q_DIR, '{}.md'.format(folder_name)), 'w') as of:
    for filename in os.listdir(os.path.join(SRC_DIR, folder_name)):
      with open(os.path.join(SRC_DIR, folder_name, filename), 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.startswith('##')]
      formatted_lines = ['# ' + ' '.join([w.capitalize() for w in filename.replace('.py', '').split('_')])]
      formatted_lines += [line[5:] if line.startswith('##   ') else line for line in lines]
      formatted_lines += [' ']
      of.write('\n'.join(formatted_lines) + '\n')

