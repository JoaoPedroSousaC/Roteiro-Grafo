
import unittest
from grafo_adj_nao_dir import Grafo

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('J-C')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-E')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-P')
        self.g_p.adicionaAresta('C-M')
        self.g_p.adicionaAresta('C-T')
        self.g_p.adicionaAresta('M-T')
        self.g_p.adicionaAresta('T-Z')


        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('J-C')
        self.g_p_sem_paralelas.adicionaAresta('C-E')
        self.g_p_sem_paralelas.adicionaAresta('C-P')
        self.g_p_sem_paralelas.adicionaAresta('C-M')
        self.g_p_sem_paralelas.adicionaAresta('C-T')
        self.g_p_sem_paralelas.adicionaAresta('M-T')
        self.g_p_sem_paralelas.adicionaAresta('T-Z')

        # Grafos completos
        #self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c = Grafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('J-C')
        self.g_c.adicionaAresta('J-E')
        self.g_c.adicionaAresta('J-P')
        self.g_c.adicionaAresta('C-E')
        self.g_c.adicionaAresta('C-P')
        self.g_c.adicionaAresta('E-P')

        self.g_c3 = Grafo(['J'])

        # Grafos com laco
        #self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('A-A')
        self.g_l1.adicionaAresta('A-A')
        self.g_l1.adicionaAresta('B-A')

        #self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('A-B')
        self.g_l2.adicionaAresta('B-B')
        self.g_l2.adicionaAresta('B-A')

        #self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('C-A')
        self.g_l3.adicionaAresta('C-C')
        self.g_l3.adicionaAresta('D-D')

        #self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l4 = Grafo(['D'])
        self.g_l4.adicionaAresta('D-D')

        #self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})
        self.g_l5 = Grafo(['C', 'D'])
        self.g_l5.adicionaAresta('D-C')
        self.g_l5.adicionaAresta('C-C')

        self.g_l6 = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])
        self.g_l6.adicionaAresta('D-G')
        self.g_l6.adicionaAresta('B-G')
        self.g_l6.adicionaAresta('E-B')
        self.g_l6.adicionaAresta('C-E')
        self.g_l6.adicionaAresta('D-A')
        self.g_l6.adicionaAresta('D-C')
        self.g_l6.adicionaAresta('D-F')
        self.g_l6.adicionaAresta('A-C')
        self.g_l6.adicionaAresta('C-F')
        self.g_l6.adicionaAresta('E-G')
        self.g_l6.adicionaAresta('E-H')
        self.g_l6.adicionaAresta('H-G')

        self.g_l7 = Grafo(['D', 'C', 'A', 'F', 'E', 'H', 'G', 'B'])
        self.g_l7.adicionaAresta('D-G')
        self.g_l7.adicionaAresta('B-G')
        self.g_l7.adicionaAresta('E-B')
        self.g_l7.adicionaAresta('C-E')
        self.g_l7.adicionaAresta('D-A')
        self.g_l7.adicionaAresta('D-C')
        self.g_l7.adicionaAresta('D-F')
        self.g_l7.adicionaAresta('A-C')
        self.g_l7.adicionaAresta('C-F')
        self.g_l7.adicionaAresta('E-G')
        self.g_l7.adicionaAresta('E-H')
        self.g_l7.adicionaAresta('H-G')
        self.g_l7.adicionaAresta('H-A')

        self.g_l8 = Grafo(['A', 'B', 'C'])
        self.g_l8.adicionaAresta('A-B')
        self.g_l8.adicionaAresta('B-C')
        self.g_l8.adicionaAresta('A-C')

        self.g_z = Grafo(['J', 'C', 'E', 'P', 'G', 'A', 'B'])
        self.g_z.adicionaAresta('J-C')
        self.g_z.adicionaAresta('E-C')
        self.g_z.adicionaAresta('E-P')
        self.g_z.adicionaAresta('G-P')
        self.g_z.adicionaAresta('A-G')
        self.g_z.adicionaAresta('A-B')


        self.g_z1 = Grafo(['J', 'U', 'V', 'I', 'T', 'O', 'R', 'E', 'P', 'B', 'L', 'C', 'A'])
        self.g_z1.adicionaAresta('J-A')
        self.g_z1.adicionaAresta('U-C')
        self.g_z1.adicionaAresta('L-V')
        self.g_z1.adicionaAresta('I-B')
        self.g_z1.adicionaAresta('P-O')
        self.g_z1.adicionaAresta('R-E')
        self.g_z1.adicionaAresta('J-U')
        self.g_z1.adicionaAresta('E-P')
        self.g_z1.adicionaAresta('A-C')
        self.g_z1.adicionaAresta('U-L')

        self.g_z2 = Grafo(['I', 'F', 'P', 'B', 'E', 'D', 'U'])
        self.g_z2.adicionaAresta('I-F')
        self.g_z2.adicionaAresta('B-F')
        self.g_z2.adicionaAresta('D-U')
        self.g_z2.adicionaAresta('B-E')
        self.g_z2.adicionaAresta('U-E')
        self.g_z2.adicionaAresta('I-F')
        self.g_z2.adicionaAresta('F-U')

        self.g_z3 = Grafo(['I', 'F','P'])
        self.g_z3.adicionaAresta('I-F')
        self.g_z3.adicionaAresta('F-F')
        self.g_z3.adicionaAresta('F-P')

        self.g_z4 = Grafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z'])
        self.g_z4.adicionaAresta('A-B')
        self.g_z4.adicionaAresta('B-C')
        self.g_z4.adicionaAresta('C-D')
        self.g_z4.adicionaAresta('D-E')
        self.g_z4.adicionaAresta('F-E')
        self.g_z4.adicionaAresta('F-G')
        self.g_z4.adicionaAresta('G-H')
        self.g_z4.adicionaAresta('I-J')
        self.g_z4.adicionaAresta('J-K')
        self.g_z4.adicionaAresta('K-L')
        self.g_z4.adicionaAresta('L-M')
        self.g_z4.adicionaAresta('N-M')
        self.g_z4.adicionaAresta('P-Q')
        self.g_z4.adicionaAresta('Z-A')
        self.g_z4.adicionaAresta('O-P')
        self.g_z4.adicionaAresta('T-S')

        self.g_z5 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g_z5.adicionaAresta('A-A')
        self.g_z5.adicionaAresta('B-A')
        self.g_z5.adicionaAresta('B-B')
        self.g_z5.adicionaAresta('A-G')
        self.g_z5.adicionaAresta('F-E')
        self.g_z5.adicionaAresta('E-G')

        self.g_z6 = Grafo(['G', 'R', 'A', 'F', 'O', 'S'])
        self.g_z6.adicionaAresta('G-R')
        self.g_z6.adicionaAresta('R-A')
        self.g_z6.adicionaAresta('A-F')
        self.g_z6.adicionaAresta('F-O')
        self.g_z6.adicionaAresta('O-S')
        self.g_z6.adicionaAresta('G-S')

        self.g_z7 = Grafo(['G'])
        self.g_z7.adicionaAresta('G-G')

        self.g_z8 = Grafo(['G', 'R', 'A', 'F', 'O', 'S', 'N', 'D', 'I', 'E', 'C'])
        self.g_z8.adicionaAresta('G-R')
        self.g_z8.adicionaAresta('A-R')
        self.g_z8.adicionaAresta('A-F')
        self.g_z8.adicionaAresta('O-F')
        self.g_z8.adicionaAresta('O-S')
        self.g_z8.adicionaAresta('N-S')
        self.g_z8.adicionaAresta('N-D')
        self.g_z8.adicionaAresta('I-D')
        self.g_z8.adicionaAresta('I-E')
        self.g_z8.adicionaAresta('E-C')
        self.g_z8.adicionaAresta('G-C')

        self.g_z9 = Grafo(['G', 'R', 'A', 'F', 'O', 'S', 'N', 'D', 'I', 'E', 'C'])
        self.g_z9.adicionaAresta('G-R')
        self.g_z9.adicionaAresta('A-R')
        self.g_z9.adicionaAresta('A-F')
        self.g_z9.adicionaAresta('O-F')
        self.g_z9.adicionaAresta('O-S')
        self.g_z9.adicionaAresta('N-S')
        self.g_z9.adicionaAresta('I-D')
        self.g_z9.adicionaAresta('C-E')
        self.g_z9.adicionaAresta('G-C')

        self.g_z10 = Grafo(['M', 'O', 'S', 'C', 'A'])
        self.g_z10.adicionaAresta('M-O')
        self.g_z10.adicionaAresta('M-A')
        self.g_z10.adicionaAresta('S-C')
        self.g_z10.adicionaAresta('A-O')
        self.g_z10.adicionaAresta('C-C')
        self.g_z10.adicionaAresta('S-A')

        self.g_z11 = Grafo(['D', 'E', 'S', 'L', 'U', 'M', 'B', 'R', 'A', 'T', 'I', 'V', 'O'])
        self.g_z11.adicionaAresta('D-E')
        self.g_z11.adicionaAresta('V-O')
        self.g_z11.adicionaAresta('S-L')
        self.g_z11.adicionaAresta('T-I')
        self.g_z11.adicionaAresta('M-U')
        self.g_z11.adicionaAresta('A-R')
        self.g_z11.adicionaAresta('B-R')
        self.g_z11.adicionaAresta('M-O')
        self.g_z11.adicionaAresta('E-S')
        self.g_z11.adicionaAresta('L-U')
        self.g_z11.adicionaAresta('I-V')
        self.g_z11.adicionaAresta('T-A')

        self.g_z12 = Grafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1'])
        self.g_z12.adicionaAresta('A-B')
        self.g_z12.adicionaAresta('A-C')
        self.g_z12.adicionaAresta('A-D')
        self.g_z12.adicionaAresta('B-E')
        self.g_z12.adicionaAresta('B-I')
        self.g_z12.adicionaAresta('B-F')
        self.g_z12.adicionaAresta('C-G')
        self.g_z12.adicionaAresta('C-D')
        self.g_z12.adicionaAresta('D-H')
        self.g_z12.adicionaAresta('E-F')
        self.g_z12.adicionaAresta('F-J')
        self.g_z12.adicionaAresta('F-G')
        self.g_z12.adicionaAresta('H-L')
        self.g_z12.adicionaAresta('H-G')
        self.g_z12.adicionaAresta('I-M')
        self.g_z12.adicionaAresta('I-J')
        self.g_z12.adicionaAresta('J-N')
        self.g_z12.adicionaAresta('K-O')
        self.g_z12.adicionaAresta('L-P')
        self.g_z12.adicionaAresta('M-Q')
        self.g_z12.adicionaAresta('M-S')
        self.g_z12.adicionaAresta('N-R')
        self.g_z12.adicionaAresta('N-S')
        self.g_z12.adicionaAresta('N-T')
        self.g_z12.adicionaAresta('O-S')
        self.g_z12.adicionaAresta('P-T')
        self.g_z12.adicionaAresta('Q-U')
        self.g_z12.adicionaAresta('Q-R')
        self.g_z12.adicionaAresta('R-V')
        self.g_z12.adicionaAresta('R-S')
        self.g_z12.adicionaAresta('S-W')
        self.g_z12.adicionaAresta('S-X')
        self.g_z12.adicionaAresta('S-T')
        self.g_z12.adicionaAresta('U-C1')
        self.g_z12.adicionaAresta('U-Y')
        self.g_z12.adicionaAresta('V-Y')
        self.g_z12.adicionaAresta('V-Z')
        self.g_z12.adicionaAresta('V-W')
        self.g_z12.adicionaAresta('W-A1')
        self.g_z12.adicionaAresta('X-A1')
        self.g_z12.adicionaAresta('X-B1')
        self.g_z12.adicionaAresta('A1-E1')
        self.g_z12.adicionaAresta('E1-D1')
        self.g_z12.adicionaAresta('D1-C1')
        self.g_z12.adicionaAresta('E1-F1')
        self.g_z12.adicionaAresta('F1-G1')
        self.g_z12.adicionaAresta('G1-E1')

        self.g_z13 = Grafo(
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1'])
        self.g_z13.adicionaAresta('A-B')
        self.g_z13.adicionaAresta('A-C')
        self.g_z13.adicionaAresta('A-D')
        self.g_z13.adicionaAresta('B-E')
        self.g_z13.adicionaAresta('B-I')
        self.g_z13.adicionaAresta('B-F')
        self.g_z13.adicionaAresta('C-G')
        self.g_z13.adicionaAresta('C-D')
        self.g_z13.adicionaAresta('D-H')
        self.g_z13.adicionaAresta('E-F')
        self.g_z13.adicionaAresta('F-J')
        self.g_z13.adicionaAresta('F-G')
        self.g_z13.adicionaAresta('H-L')
        self.g_z13.adicionaAresta('H-G')
        self.g_z13.adicionaAresta('I-M')
        self.g_z13.adicionaAresta('I-J')
        self.g_z13.adicionaAresta('J-N')
        self.g_z13.adicionaAresta('K-O')
        self.g_z13.adicionaAresta('L-P')
        self.g_z13.adicionaAresta('M-Q')
        self.g_z13.adicionaAresta('M-S')
        self.g_z13.adicionaAresta('N-R')
        self.g_z13.adicionaAresta('N-S')
        self.g_z13.adicionaAresta('N-T')
        self.g_z13.adicionaAresta('O-S')
        self.g_z13.adicionaAresta('P-T')
        self.g_z13.adicionaAresta('Q-U')
        self.g_z13.adicionaAresta('Q-R')
        self.g_z13.adicionaAresta('R-V')
        self.g_z13.adicionaAresta('R-S')
        self.g_z13.adicionaAresta('S-W')
        self.g_z13.adicionaAresta('S-X')
        self.g_z13.adicionaAresta('S-T')
        self.g_z13.adicionaAresta('U-C1')
        self.g_z13.adicionaAresta('U-Y')
        self.g_z13.adicionaAresta('V-Y')
        self.g_z13.adicionaAresta('V-Z')
        self.g_z13.adicionaAresta('V-W')
        self.g_z13.adicionaAresta('W-A1')
        self.g_z13.adicionaAresta('X-A1')
        self.g_z13.adicionaAresta('X-B1')
        self.g_z13.adicionaAresta('A1-E1')
        self.g_z13.adicionaAresta('E1-D1')
        self.g_z13.adicionaAresta('D1-C1')
        self.g_z13.adicionaAresta('E1-F1')
        self.g_z13.adicionaAresta('F1-G1')
        self.g_z13.adicionaAresta('G1-E1')
        self.g_z13.adicionaAresta('A-F1')
        self.g_z13.adicionaAresta('G1-F1')


    def test_Algoritmo_de_Dijkstra(self):
        '''----G_Z13----'''
        self.assertFalse(self.g_z13.Algoritmo_de_Dijkstra('A', 'G1', 1, 3, ['L', 'S', 'U', 'D1']))
        self.assertEqual(set(self.g_z13.Algoritmo_de_Dijkstra('A', 'G1', 2, 3, ['L', 'S', 'U', 'D1'])),
                         set('A -> F1 -> G1'))
        '''----G_Z12----'''
        self.assertFalse(self.g_z12.Algoritmo_de_Dijkstra('A','G1',2,3,['L','S','U','D1']))
        self.assertEqual(set(self.g_z12.Algoritmo_de_Dijkstra('A','G1',3,3,['L','S','U','D1'])), set('A -> D -> H -> L -> P -> T -> S -> M -> Q -> U -> C1 -> D1 -> E1 -> G1'))

        '''----G_Z11----'''
        self.assertFalse(self.g_z11.Algoritmo_de_Dijkstra('D','O',2,3, ['L','R','I']))
        self.assertEqual(set(self.g_z11.Algoritmo_de_Dijkstra('D','O',3,3, ['L','R','I'])),
                         set('D -> E -> S -> L -> U -> M -> O'))

        '''----G_Z10----'''

        self.assertFalse(self.g_z10.Algoritmo_de_Dijkstra('M','C',1,2,['S']))
        self.assertEqual(set(self.g_z10.Algoritmo_de_Dijkstra('M','C',2,2,['S'])),
                         set('M -> A -> S -> C'))

        '''----G_Z9----'''

        self.assertFalse(self.g_z9.Algoritmo_de_Dijkstra('G','O',2,2,['A','S','I']))
        self.assertEqual(set(self.g_z9.Algoritmo_de_Dijkstra('G','O',4,4,['A','S','I'])),
                         set('G -> R -> A -> F -> O'))

        '''----G_Z8----'''

        self.assertFalse(self.g_z8.Algoritmo_de_Dijkstra('G','D',1,2,['A','S','E']))
        self.assertEqual(set(self.g_z8.Algoritmo_de_Dijkstra('G', 'D', 2, 2, ['A', 'S', 'E'])),
                         set('G -> C -> E -> I -> D'))

        '''----G_Z6----'''

        self.assertFalse(self.g_z6.Algoritmo_de_Dijkstra('G','F',0,2,['R','F']))
        self.assertEqual(set(self.g_z6.Algoritmo_de_Dijkstra('G', 'F', 2, 2, ['R','F'])),
                         set('G -> R -> A -> F'))

        '''----G_Z5----'''

        self.assertFalse(self.g_z5.Algoritmo_de_Dijkstra('A','F',2,2,['A','F']))
        self.assertEqual(set(self.g_z5.Algoritmo_de_Dijkstra('A','F',3,3,['A','F'])),
                         set('A -> G -> E -> F'))

        '''----G_Z4----'''

        self.assertFalse(self.g_z4.Algoritmo_de_Dijkstra('A','H',3,3,['D','J']))
        self.assertEqual(set(self.g_z4.Algoritmo_de_Dijkstra('A','H',4,4,['D','J'])),
                         set('A -> B -> C -> D -> E -> F -> G -> H'))

        '''----G_Z3----'''

        self.assertFalse(self.g_z3.Algoritmo_de_Dijkstra('I','P',1,1,['P']))
        self.assertEqual(set(self.g_z3.Algoritmo_de_Dijkstra('I','P',2,2,['P'])),
                         set('I -> F -> P'))

        '''----G_Z2----'''

        self.assertFalse(self.g_z2.Algoritmo_de_Dijkstra('I','U',1,0,['F']))
        self.assertEqual(set(self.g_z2.Algoritmo_de_Dijkstra('I','U',1,1,['F'])),
                         set('I -> F -> U'))

        '''----G_Z1----'''

        self.assertFalse(self.g_z1.Algoritmo_de_Dijkstra('J','L',2,2,['V','T','C']))
        self.assertEqual(set(self.g_z1.Algoritmo_de_Dijkstra('J','L',3,3,['V','T','C'])),
                         set('J -> U -> L'))

        '''----G_Z----'''

        self.assertFalse(self.g_z.Algoritmo_de_Dijkstra('J','B',1,1,['E','G']))
        self.assertEqual(set(self.g_z.Algoritmo_de_Dijkstra('J','B',2,2,['E','G'])),
                         set('J -> C -> E -> P -> G -> A -> B'))

        '''----G_l7----'''

        self.assertFalse(self.g_l7.Algoritmo_de_Dijkstra('D','E',1,1,['F','H']))
        self.assertEqual(set(self.g_l7.Algoritmo_de_Dijkstra('D','E',2,2,['F','H'])),
                         set('D -> A -> H -> E'))

        '''----G_l6----'''

        self.assertFalse(self.g_l6.Algoritmo_de_Dijkstra('D','E',1,1,['F','H']))
        self.assertEqual(set(self.g_l6.Algoritmo_de_Dijkstra('D','E',2,2,['F','H'])),
                         set('D -> G -> H -> E'))

        '''----PARAIBA----'''

        self.assertFalse(self.g_p.Algoritmo_de_Dijkstra('J','Z',1,2,['M']))
        self.assertEqual(set(self.g_p.Algoritmo_de_Dijkstra('J','Z',2,2,['M'])),
                         set('J -> C -> M -> T -> Z'))








