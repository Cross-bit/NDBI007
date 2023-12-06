import pandas as pd

class Page:
    def __init__(self, pointers, local_depth = 0, size = 3):
        self.local_depth = local_depth;
        self.size = size; # the n from slides
        self.data = []

        # this is basically list of indexes that points to this page, 
        # so when we split we immediatelly know which pages will play role in it (probably could be done more efficiently... (in terms of memory))
        self.page_pointers = pointers 


    def get_size(self):
        return len(self.data)

    def insert(self, value):
        self.data.append(value)

    def get_local_depth(self):
        return self.local_depth
    
    def get_data(self):
        return self.data

    # page overflown
    def is_full(self):
        return len(self.data) == self.size

    def set_pointer(self, pointer):
        self.page_pointers.append(pointer)

    def get_pointers_copy(self):
        return list(self.page_pointers)
    
    def delete_all_pointers(self):
        return self.page_pointers.clear()

    def print_info(self):
        print("page info:")
        print(f"    local depth: {self.local_depth}, capacity(n): {self.size}")
        print(f"    page data: {self.data}")
        print(f"    pointers to this page: {self.page_pointers}")


class FaginAlgorithm():

    def __init__(self):
        self.global_depth = 1
        self.global_directory = []
    
    def get_least_significant_bits(self, number, n):
        mask = (1 << n) - 1 
        least_significant = number & mask 
        return least_significant
    
    def double_directory_size(self, global_directory):
        self.global_depth

        self.global_depth += 1

        original_size = len(global_directory)

        new_pages = []

        for page in global_directory:
            new_pages.append(page);
            new_pointer_index = original_size + len(new_pages) - 1
            page.set_pointer(new_pointer_index);

        global_directory.extend(new_pages)

    def init_fagin(self):
        # we create empty page and point free pointers to it
        init_page = Page([0, 1]);
        self.global_directory.append(init_page)
        self.global_directory.append(init_page)

    ## splitting page operation
    def split_page(self, page_to_split, global_directory):
        new_local_depth = page_to_split.get_local_depth() + 1

        page_pointers = page_to_split.get_pointers_copy()
        #page_to_split.delete_all_pointers() this is probably not needed actually... we recreate the page...

        origina_page_data = page_to_split.get_data()

        new_pages_list = []

        # splitting phase
        for pointer in page_pointers:
            directory_index = self.get_least_significant_bits(pointer, self.global_depth);  # this could be cached ...
            new_page = Page([directory_index], new_local_depth) # we also recreate original page ...
            global_directory[directory_index] = new_page

            new_pages_list.append(new_page)
        

        # redistribution(/reinsertion) phase
        for value in origina_page_data:
            self.insert_value(value, global_directory)    


    def insert_value(self, value, global_directory):
        print("------------------------------")

        directory_index = self.get_least_significant_bits(value, self.global_depth);

        print(f"inserting: {value}")

        print(f"directory index: {directory_index}")

        page = global_directory[directory_index]

        if (page.is_full()):
            print(f"page overflow!!")
            local_depth = page.get_local_depth()
            if (local_depth < self.global_depth):
                print(f"splitting page")
                # we can split
                self.split_page(page, global_directory)
                self.insert_value(value, global_directory)
            elif (local_depth == self.global_depth):
                print(f"expanding directory")
                # we have to double the global directory
                self.double_directory_size(global_directory);

                print(f"inserting after expansion")
                # and try to reinsert the value
                self.insert_value(value, global_directory);
        else:
            print(f"page have space, directly inserting")
            # we can insert item
            page.insert(value)
            page.print_info();

    def insert_values(self, values):
        for value in values: 
            self.insert_value(value, self.global_directory)

    def print_structure(self): 
        print("####################################")
        print("General info:")
        print(f"Global directory depth: {self.global_depth}")
        print()
        print("##############################")
        print("pages:")
        print("##############################")
        for page in self.global_directory:
            print(f"Page data structure ")
            page.print_info()
            print("--------------------------")


# using global value for tracking global directory depth...
# (ugly... but working...)
#global_depth = 1
#
#global_directory = []
#
#def get_least_significant_bits(number, n):
#    mask = (1 << n) - 1 
#    least_significant = number & mask 
#    return least_significant
#
#
### Fagin datastructure initialisation
#def init_fagin():
#    # we create empty page and point free pointers to it
#    init_page = Page([0, 1]);
#    global_directory.append(init_page)
#    global_directory.append(init_page)
#
#
#
### expands the directory
#def double_directory_size(global_directory):
#    global global_depth
#
#    global_depth += 1
#
#    original_size = len(global_directory)
#
#    new_pages = []
#
#    for page in global_directory:
#        new_pages.append(page);
#        new_pointer_index = original_size + len(new_pages) - 1
#        page.set_pointer(new_pointer_index);
#
#    global_directory.extend(new_pages)
#    
### splitting page operation
#def split_page(page_to_split, global_directory):
#    global global_depth
#
#    new_local_depth = page_to_split.get_local_depth() + 1
#
#    page_pointers = page_to_split.get_pointers_copy()
#    #page_to_split.delete_all_pointers() this is probably not needed actually... we recreate the page...
#
#    origina_page_data = page_to_split.get_data()
#
#    new_pages_list = []
#
#    # splitting phase
#    for pointer in page_pointers:
#        directory_index = get_least_significant_bits(pointer, global_depth);  # this could be cached ...
#        new_page = Page([directory_index], new_local_depth) # we also recreate original page ...
#        global_directory[directory_index] = new_page
#
#        new_pages_list.append(new_page)
#    
#
#    # redistribution(/reinsertion) phase
#    for value in origina_page_data:
#        insert(value, global_directory)    
#
#
#
#
#def insert(value, global_directory):
#    print("------------------------------")
#
#    global global_depth
#
#    directory_index = get_least_significant_bits(value, global_depth);
#
#    print(f"inserting: {value}")
#
#    print(f"dir index: {directory_index}")
#
#    page = global_directory[directory_index]
#
#    if (page.is_full()):
#        print(f"page overflow!!")
#        local_depth = page.get_local_depth()
#        if (local_depth < global_depth):
#            print(f"splitting page")
#            # we can split
#            split_page(page, global_directory)
#            insert(value, global_directory)
#        elif (local_depth == global_depth):
#            print(f"expanding directory")
#            # we have to double the global directory
#            double_directory_size(global_directory);
#
#            print(f"inserting after expansion")
#            # and try to reinsert the value
#            insert(value, global_directory);
#    else:
#        print(f"page have space, directly inserting")
#        # we can insert item
#        page.insert(value)
#        page.print_info();
#
#
#def print_final_structure(global_directory):
#    
#    global global_depth
#    print("####################################")
#    print("General info:")
#    print(f"Global directory depth: {global_depth}")
#    print()
#    print("##############################")
#    print("pages:")
#    print("##############################")
#    for page in global_directory:
#        print(f"Page data structure ")
#        page.print_info()
#        print("--------------------------")
#
#
#def insert_multiple_values(values, global_directory):
#    for value in values: 
#        insert(value, global_directory)

## Running fagin

## read csv data using pandas
data = pd.read_csv('records_A3.csv')

students_ids_frame = data['Student_ID']

student_ids = students_ids_frame.to_list()

fagin = FaginAlgorithm()

fagin.init_fagin()

fagin.insert_values(student_ids)


# Uncomment this to print final structure

#fagin.print_structure()


# Uncomment this to print fagin example from the lecture

# Test insertions from the lecture
#first.insert_values([20, 11, 8, 27, 19, 5, 24, 32])
#fagin.print_structure()


