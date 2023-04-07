import unittest
from lca.todo import *
from os.path import dirname, realpath, join, normpath
from os import listdir
from ast import literal_eval
import signal

TIMEOUT = 60 # seconds

test_path = normpath(join(dirname(realpath(__file__)),"test_data","checking"))
test_cases = ['binary_small','binary_large','dag_small','dag_large','multi_small','multi_large']

class Tests_01(unittest.TestCase):
    def test_01_sanity(self):
        # test reading sample inputs
        for case in test_cases:
            test_file = normpath(join(test_path,case + ".in")) 
            try:
                with open(test_file) as f:
                    parent = literal_eval(f.read())
            except:        
                    self.assertTrue(False,msg="Couldn't read the sample input file " + test_file + "!")

    def test_02_sanity(self):
        # test reading sample outputs
        for case in test_cases:    
            test_file = normpath(join(test_path,case + ".out"))
            try:
                with open(test_file) as f:
                    lcas = literal_eval(f.read())
            except:        
                self.assertTrue(False,msg="Couldn't read the sample output file " + test_file + "!")


    def __run_case__(self,case):
        sample_in = normpath(join(test_path,case + ".in"))
        sample_out = normpath(join(test_path,case + ".out"))

        with open(sample_in,'r') as f:
            parent = literal_eval(f.read())
        with open(sample_out,'r') as f:
            lcas_sln = literal_eval(f.read()) 
        
        try:
            signal.alarm(TIMEOUT)
            lcas_student = find_LCAs(parent)
            signal.alarm(0)
        except: 
            self.assertTrue(False,msg="Couldn't run find_LCAs on input file " + sample_in + "!")
        
        for u in parent:
            for v in parent:
                self.assertTrue(u in lcas_student and v in lcas_student,msg="Failed test case " + case + ": missing LCAs for pair (" + u + "," + v + ")")
                expect = set(lcas_sln[u][v])
                answer = set(lcas_student[u][v])                
                self.assertTrue(expect == answer, msg="Failed test case " + case + ": wrong LCAs for pair (" + u + "," + v + ")")

    def test_04_correctness(self):
        # test binary small
        self.__run_case__('binary_small')
    
    def test_05_correctness(self):
        # test binary large
        self.__run_case__('binary_large')
        
    def test_06_correctness(self):
        # test dag small
        self.__run_case__('dag_small')
    
    def test_06_correctness(self):
        # test dag large
        self.__run_case__('dag_large')
    
    def test_07_correctness(self):
        # test multifurcating small
        self.__run_case__('multi_small')

    def test_08_correctness(self):
        # test multifurcating large
        self.__run_case__('multi_large')
