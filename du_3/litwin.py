import pandas as pd

class Page:
    def __init__(self, capacity = 3):
        self.data = []
        self.capacity = capacity
        self.was_split_in_stage = False
        # page splitting occures after this many inserts

    def insert_value(self, value):
        self.data.append(value)
        
    def get_data(self):
        return self.data;

    ## removes only the first occurence
    def remove_value(self, value):
        self.data.remove(value);

    def set_split_state(self, value):
        self.was_split_in_stage = value

    def get_split_state(self):
        return self.was_split_in_stage

class LitwinAlgorithm:

    def __init__(self):
        self.stage = 0
        self.split_treshold = 2
        self.pages = []
        self.total_insertions_ctr = 0
        self.current_pointer_index = 0


    def get_least_significant_bits(self, number, n):
        
        mask = (1 << n) - 1 
        least_significant = number & mask 
        return least_significant
    
    def litwin_init(self):
        init_page = Page()
        self.pages.append(init_page)

    
    def split_page(self):
        print(f"splitting page at index {self.current_pointer_index}")

        new_page = Page()
        new_page.set_split_state(True)

        self.pages.append(new_page)

        # redistribute values from last page

        pageValues = list(self.pages[self.current_pointer_index].get_data());

        self.pages[self.current_pointer_index].set_split_state(True)

        print(f"redistributing values ")
        for value in pageValues:
            new_page_index = self.get_least_significant_bits(value, self.stage + 1);
            self.pages[new_page_index].insert_value(value)
            self.pages[self.current_pointer_index].remove_value(value);
            

        # we move the pointer after split
        self.current_pointer_index += 1

    def print_structure(self):
        for i, page in enumerate(self.pages):
            print(f" {i}: {page.get_data()}")


    def get_page_index(self, new_value):
        # we need to decide based on how many bits we will decide (stage or stage + 1)
        
        page_index = self.get_least_significant_bits(new_value, self.stage)

        if (self.pages[page_index].get_split_state()):
            page_index = self.get_least_significant_bits(new_value, self.stage + 1)

        return page_index

    def update_stage(self):
        print(f"updating stage")
        # new stage starts
        self.stage += 1;

        for page in self.pages:
            page.set_split_state(False)

        # reset the pointer index
        self.current_pointer_index = 0 


    def insert_values(self, values_to_insert):

        self.total_insertions_ctr = 0
        self.current_pointer_index = 0

        for new_value in values_to_insert:

            self.total_insertions_ctr += 1;
            
            page_index = self.get_page_index(new_value)


            print(f"inserting {new_value} into page {page_index}")

            # else we insert new value to the page pointed by the pointer
            self.pages[page_index].insert_value(new_value)
            # print(f"{pages[page_index].get_data()}")

            if (self.total_insertions_ctr >= 2) and (self.total_insertions_ctr % self.split_treshold) == 0:
                self.split_page();


            if (len(self.pages) == pow(2, self.stage + 1)):
                print(f"updating stage")
                # new stage starts
                self.stage += 1;

                for page in self.pages:
                    page.set_split_state(False)

                # reset the pointer index
                self.current_pointer_index = 0 

            print(f"current stage ${self.stage}")
            print(f"current pointer index ${self.current_pointer_index}")

            self.print_structure()




first = LitwinAlgorithm()
first.litwin_init()


## Running fagin

## read csv data using pandas
data = pd.read_csv('records_A3.csv')

students_ids_frame = data['Student_ID']

student_ids = students_ids_frame.to_list()

first.insert_values(student_ids)

# Uncomment this to print litwin example from the lecture

# Testing values from the lecture:
# first.run_litwin([20, 11, 8, 3, 24, 32, 27, 19, 10, 5])

