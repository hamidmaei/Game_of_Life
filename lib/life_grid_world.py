import random

class GridLife(object):

    def __init__(self,n_rows=100,n_columns=100):

            '''n_rows is the number of rows and n_columns is the number of columns of the grid world'''
            self.n_rows = n_rows
            self.n_columns = n_columns

    def init_grid_world(self):

            random_matrix = [[round(random.random()) for  x in range(self.n_columns)] for x in range(self.n_rows)]

            return random_matrix

    def get_index(self,pos):

            i,j = pos[0],pos[1]

            if i>self.n_columns-1:
                        i = 0

            if i<0:
                        i = self.n_columns-1

            if j>self.n_rows-1:
                        j = 0

            if j < 0:
                        j = self.n_rows-1

            return [i,j]

    def get_8neighbors_status_vec(self,matrix,pos):

            m  = len(matrix)
            n   = len(matrix[0])
            i, j = pos[0],pos[1]

            pos_down   = self.get_index([i+1,j])
            pos_up       = self.get_index([i-1,j])
            pos_right    = self.get_index([i,j+1])
            pos_left      =  self.get_index([i,j-1])

            pos_diag_up_right      = self.get_index([i-1,j+1])
            pos_diag_up_left        = self.get_index([i-1,j-1])
            pos_diag_down_right  = self.get_index([i+1,j+1])
            pos_diag_down_left    =  self.get_index([i+1,j-1])

            neighbors_pos_vec    = [pos_down,pos_up,pos_right,pos_left,pos_diag_up_right,pos_diag_up_left,pos_diag_down_right,pos_diag_down_left]

            neighbors_status_vec = []

            for _pos in neighbors_pos_vec:

                        neighbors_status_vec.append(matrix[ _pos[0] ] [ _pos[1] ])

            return neighbors_status_vec


    def apply_rule_get_pos_status(self,matrix,pos):

            pos_status                  = matrix[pos[0]][pos[1]]
            neighbors_status_vec = self.get_8neighbors_status_vec(matrix,pos)
            total_live                    = sum(neighbors_status_vec)

            if pos_status==1:

                        if total_live in [0,1,4,5,6]:

                                    pos_status = 0

            if pos_status == 0:

                        if total_live ==3:

                                    pos_status = 1



            return pos_status

    def set_next_state_matrix(self,state_matrix):

        m = len(state_matrix)
        n =  len(state_matrix[0])

        next_state_matrix = [[0 for x in range(n)] for x in range(m)]

        for i in range(m):
            for j in range(n):
                pos = [i,j]
                next_state_matrix[i][j] = self.apply_rule_get_pos_status(state_matrix,pos)

        return next_state_matrix
