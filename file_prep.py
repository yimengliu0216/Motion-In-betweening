import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import yaml
import time
import shutil

if __name__ == '__main__':
    opt = yaml.load(open('./config/train-base.yaml', 'r').read())

    stamp = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    stamp  = stamp + '-' + opt['train']['method']

    if opt['train']['debug']:
        stamp = 'debug'
    log_dir = os.path.join('./log', stamp)
    model_dir = os.path.join('./model', stamp)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)
    def copydirs(from_file, to_file):
        if not os.path.exists(to_file):  
            os.makedirs(to_file)
        files = os.listdir(from_file)  
        for f in files:
            if os.path.isdir(from_file + '/' + f):  
                copydirs(from_file + '/' + f, to_file + '/' + f)  
            else:
                if '.git' not in from_file:
                    shutil.copy(from_file + '/' + f, to_file + '/' + f) 
    copydirs('./', log_dir + '/src')

    